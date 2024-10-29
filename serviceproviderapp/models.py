from django.db import models
from django.conf import settings

# Create your models here.
class ServiceProviders(models.Model): 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  primary_key=True)
    username = models.CharField(max_length = 50)
    img = models.ImageField(default='images/services/service.png', blank = True, upload_to = "images/services/")
    contact_email =  models.EmailField(max_length = 254)
    contact_phone =  models.CharField(max_length = 15)
    service_type = models.CharField(max_length=20)
    price = models.FloatField()
    bio = models.CharField("Bio", max_length=1024)
    address = models.CharField("Address", max_length=1024)
    city = models.CharField("City", max_length=1024)
    zip_code = models.CharField("ZIP / Postal code", max_length=12)
    rating = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    total_rating = models.IntegerField(default=0)
    total_reviews = models.IntegerField(default=0)
    is_service_profile_complete  = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)

class ServicesOrder(models.Model):

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length = 254)
    customer_latitude = models.FloatField(default=0)
    customer_longitude = models.FloatField(default=0)
    provider = models.ForeignKey(ServiceProviders, on_delete=models.CASCADE)
    provider_name = models.CharField(max_length = 254)
    is_active = models.BooleanField(default=True)
    is_accepted = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    service_time = models.DateTimeField(auto_now_add=True)
