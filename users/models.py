from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
from PIL import Image
from django.db.models.signals import post_save


def user_directory_path_profile(instance, filename):
    ''' colocamos el {0} para usarlo con el format que va a ser referencia al 0
        llamamos a la instancia, le decimos de la profile, de su user que capture el username 
        para que ese sea el nombre que va a ir en lugar del 0'''
    profile_picture_name = 'users/{0}/profile.jpg'.format(
        instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_picture_name


def user_directory_path_banner(instance, filename):
    ''' colocamos el {0} para usarlo con el format que va a ser referencia al 0
        llamamos a la instancia, le decimos de la profile, de su user que capture el username 
        para que ese sea el nombre que va a ir en lugar del 0'''
    profile_picture_name = 'users/{0}/banner.jpg'.format(
        instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_picture_name

class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(default='img/logo.png', upload_to=user_directory_path_profile)
    banner = models.ImageField(default='img/banner.jpg', upload_to=user_directory_path_banner)
    date_created = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length= 15, null = True, blank=True)
    occupation = models.CharField(max_length=80, null=True, blank=True)
    studies = models.CharField(max_length=80, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    biography = models.TextField(max_length=150, null=True, blank=True)
    
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
 
post_save.connect(create_user_profile, sender=User)  
post_save.connect(save_user_profile, sender=User)     
