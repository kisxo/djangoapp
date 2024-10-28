from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from .models import ServiceProviders
from django.conf import settings
from .forms import ServiceProfileForm

@login_required
def servicedashboard(request):
    return render(request, "serviceproviderapp/dashboard.html")

@login_required
def accounttype(request, option):
    if request.method == "POST" and request.user.check_password(request.POST['password']):
        if option == 'become_provider':
            request.user.is_service_provider = True
        elif option == 'delete_service':
            request.user.is_service_provider = False
            
    request.user.save()
    return HttpResponseRedirect('/profile')

@login_required
def serviceproviderprofile(request):
    if not request.user.is_service_provider:
        return HttpResponseRedirect('/')
    
    services_list = [
        "Electrician",
        "Plumber",
        "Carpenter",
        "Mason",
        "Welder",
        "Mechanic",
        "Painter",
        "Landscaper",
        "Pest Control"
    ]
    return render(request, "serviceproviderapp/profile.html", {'services': services_list})

@login_required
def serviceproviderupdate(request, field):

    current_serviceprovider = ServiceProviders.objects.get_or_create(user = request.user)
    current_serviceprovider = ServiceProviders.objects.get(user = request.user)
    if request.method == "POST":
        match field:
            case 'contact':
                current_serviceprovider.contact_email = request.POST.get("contact_email")
                current_serviceprovider.contact_phone = request.POST.get("contact_phone")
            case 'service_type':
                current_serviceprovider.service_type = request.POST.get("service_type")
            case 'bio':
                current_serviceprovider.bio  = request.POST.get("bio")
            case 'address':
                current_serviceprovider.address  = request.POST.get("address")
                current_serviceprovider.city  = request.POST.get("city")
                current_serviceprovider.zip_code  = request.POST.get("zip_code")
            case 'coords':
                if not request.POST.get("latitude") and not request.POST.get("longitude"):
                    return HttpResponseRedirect('/serviceproviders/serviceproviderprofile/')
                else:
                    current_serviceprovider.latitude  = request.POST.get("latitude")
                    current_serviceprovider.longitude  = request.POST.get("longitude")
            case 'is_available':
                # current_serviceprovider.is_available = request.POST.get("is_available")
                if request.POST.get("is_available") == 'on':
                    current_serviceprovider.is_available = True
                else:
                    current_serviceprovider.is_available = False

            case _:
                pass
  
        current_serviceprovider.save()
        return HttpResponseRedirect('/serviceproviders/serviceproviderprofile/')

    
@login_required
def bookservice(request, id):
    if request.method == "POST":
        print("post method book")
        pass

    return render(request, 'serviceproviderapp/bookservice.html', { 'id': id})