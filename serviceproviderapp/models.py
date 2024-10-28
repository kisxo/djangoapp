from django.db import models
from django.conf import settings

# Create your models here.
class ServiceProviders(models.Model): 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  primary_key=True)
    contact_email =  models.EmailField(max_length = 254)
    service_type = models.CharField(max_length=20)
    rating = models.FloatField(default=0)
    total_rating = models.IntegerField(default=0)
    total_reviews = models.IntegerField(default=0)
    is_service_profile_complete  = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
