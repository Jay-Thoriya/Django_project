from django.db import models
from django.contrib.auth.models import User
from email.policy import default

from localflavor.us.models import USStateField, USZipCodeField


from .utils import users_directory_path


class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = USStateField(default="NY")
    zip_code = USZipCodeField(blank=True)

    def __str__(self):
        return f'Location {self.id}'

class Profile(models.Model):
    users = models.OneToOneField(User , on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=users_directory_path,null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(
        Location, on_delete=models.SET_NULL, null=True)    

    def __str__(self):
        return F'{self.users.username}\'s Profile'
    
