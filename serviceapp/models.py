from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_picture = models.ImageField( default='images/profile_pictures/profile.jpg', blank = True, upload_to = "images/profile_pictures/")
    contact_phone = models.CharField(max_length=10)
    address = models.CharField("Address", max_length=1024)
    zip_code = models.CharField("ZIP / Postal code", max_length=12)
    city = models.CharField("City", max_length=1024,)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    is_profile_complete  = models.BooleanField(default=False)
    is_service_provider = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.id}, {self.username}, {self.address}'
    