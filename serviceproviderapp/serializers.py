from rest_framework import serializers
from .models import ServiceProviders

class ServiceProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProviders
        fields = '__all__'  