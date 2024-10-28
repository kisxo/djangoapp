from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core import serializers
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

def index(request):
  
  return render(request, "serviceapp/index.html")

# @login_required
# def updateProfile(request):
#   submitted = False
#   if request.method == "POST":
#     form = ProfileForm(request.POST)
#     if form.is_valid():
#       new_profile_form = form.save(commit=False)
#       Fruit.objects.create(name="Apple")
#       Profile.objects.create()
#       return HttpResponseRedirect('/updateProfile?submitted=True')
#   else:
#     form = ProfileForm
#     if 'submitted' in request.GET:
#       submitted = True

#   context_data = { 'form': form, 
#                    'submitted': submitted}
#   return render(request, "serviceapp/updateProfile.html", context_data)

@login_required
def profile(request):
  return render(request, "serviceapp/profile.html")

@login_required
def updateProfile(request, field):

  if request.method == "POST":

    match field:
      case 'profile_picture':
        request.user.profile_picture = request.FILES.get("profile_picture")
      case 'first_name':
        request.user.first_name = request.POST.get("first_name")
      case 'last_name':
        request.user.last_name = request.POST.get("last_name")
      case _:
          pass
      
    request.user.save()
    return HttpResponseRedirect('/profile')
  else:
    return HttpResponseRedirect('/profile')