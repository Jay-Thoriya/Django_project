# Generated by Django 4.2.4 on 2023-08-23 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='users',
            new_name='user',
        ),
    ]
