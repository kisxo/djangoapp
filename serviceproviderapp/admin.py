from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ServiceProviders, ServicesOrder

admin.site.register(ServiceProviders)
admin.site.register(ServicesOrder)