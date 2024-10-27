from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from . forms import ProfileForm
from . models import Profile
from django.core import serializers
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

def index(request):
  
  if request.user.is_authenticated:
    profile = Profile(request.user)
    # print(request.user.profile.address)

  context_data = {}#request.user.profile}
  print(context_data)
  return render(request, "serviceapp/index.html", context_data)

@login_required
def updateProfile(request):
  submitted = False
  if request.method == "POST":
    form = ProfileForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/updateProfile?submitted=True')
  else:
    form = ProfileForm
    if 'submitted' in request.GET:
      submitted = True

  context_data = { 'form': form, 
                   'submitted': submitted}
  return render(request, "serviceapp/updateProfile.html", context_data)