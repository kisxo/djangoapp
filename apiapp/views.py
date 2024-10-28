from django.core import serializers
import json
from serviceproviderapp.models import ServiceProviders
from django.http import HttpResponse
from serviceproviderapp.serializers import ServiceProvidersSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class ServicesView(APIView):
    def get(self, request):
        obj = ServiceProviders.objects.all()
        serializer = ServiceProvidersSerializer(obj, many=True)
        return Response(serializer.data)
