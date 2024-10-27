from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from . forms import UserProfileForm
from . models import Profile

def index(request):
  context_data = {}
  if request.user.is_authenticated:
    context_data["profile"] = Profile(request.user)

  return render(request, "serviceapp/index.html", context_data)

def updateProfile(request):
  form = UserProfileForm()
  context_data = {'form': form}
  return render(request, "serviceapp/updateProfile.html", context_data)