from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from . forms import UserProfileForm

def index(request):
  return render(request, "serviceapp/index.html")

def updateuserprofile(request):
  form = UserProfileForm()
  context_data = {'form': form}
  return render(request, "serviceapp/UpdateUserProfile.html", context_data)