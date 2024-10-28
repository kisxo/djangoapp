from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_picture = models.ImageField( default='images/profile_pictures/profile.jpg', blank = True, upload_to = "images/profile_pictures/")
    is_service_provider = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.id}, {self.email}, {self.first_name} {self.last_name}, '
    