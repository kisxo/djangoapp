from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  primary_key=True)
    profile_picture = models.ImageField( null = True, blank = True, upload_to = "images/profile_pictures/")
    contact_phone = models.CharField(max_length=10)
    address = models.CharField("Address", max_length=1024)
    zip_code = models.CharField("ZIP / Postal code", max_length=12)
    city = models.CharField("City", max_length=1024,)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    is_profile_complete  = models.BooleanField(default=False)
    is_service_providers = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

class ServiceProviders(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE,  primary_key=True)
    contact_email =  models.EmailField(max_length = 254)
    service_type = models.CharField(max_length=20)
    rating = models.FloatField(default=0)
    total_rating = models.IntegerField(default=0)
    total_reviews = models.IntegerField(default=0)
    is_service_profile_complete  = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
