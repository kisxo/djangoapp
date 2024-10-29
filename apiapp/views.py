from django.core import serializers
import json
from serviceproviderapp.models import ServiceProviders
from django.http import HttpResponse
from serviceproviderapp.serializers import ServiceProvidersSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes


# Create your views here.
@authentication_classes([])
@permission_classes([])
class ServicesView(APIView):
    def get(self, request):
        obj = ServiceProviders.objects.all()
        serializer = ServiceProvidersSerializer(obj, many=True)
        return Response(serializer.data)
