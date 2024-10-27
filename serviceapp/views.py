from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from . forms import UserProfileForm
from . models import Profile
from django.core import serializers
from django.forms.models import model_to_dict

def index(request):
  
  if request.user.is_authenticated:
    profile = Profile(request.user)
    # print(request.user.profile.address)

  context_data = {}#request.user.profile}
  print(context_data)
  return render(request, "serviceapp/index.html", context_data)

def updateProfile(request):
  form = UserProfileForm()
  context_data = {'form': form}
  return render(request, "serviceapp/updateProfile.html", context_data)