from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ServiceProviders

admin.site.register(ServiceProviders)