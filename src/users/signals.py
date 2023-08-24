from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile, Location


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(users=instance)

@receiver(post_save, sender=Profile)
def create_Profile_location(sender, instance, created, **kwargs):
    if created:
        Location.objects.create(profile=instance)
        instance.location = profile_location
        instance.save()