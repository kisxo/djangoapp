from django.contrib import admin
from .models import Profile, ServiceProviders

# Register your models here.
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'address')
admin.site.register(Profile)

# class ServiceProvidersAdmin(admin.ModelAdmin):
#     list_display = ('user',)
admin.site.register(ServiceProviders)