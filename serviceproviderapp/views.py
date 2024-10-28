from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from .models import ServiceProviders
from django.conf import settings

@login_required
def serviceproviderhome(request):
    
    if not request.user.is_service_provider:
        return HttpResponseRedirect('/serviceproviders/serviceproviderprofile')

@login_required
def serviceproviderprofile(request):

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
    return render(request, "serviceproviderapp/serviceproviderregister.html", {'services': services_list})

@login_required
def serviceproviderregister(request, field):

    current_serviceprovider = ServiceProviders.objects.get_or_create(user = request.user)
    current_serviceprovider = ServiceProviders.objects.get(user = request.user)
    if request.method == "POST":

        match field:
            case 'service_type':
                current_serviceprovider.service_type = request.POST.get("service_type")
            case 'contact':
                request.user.contact_phone = request.POST.get("contact_phone")
                current_serviceprovider.contact_email = request.POST.get("contact_email")
            case 'address':
                request.user.address = request.POST.get("address")
            case 'is_availabe':
                current_serviceprovider.is_available = request.POST.get("is_available")
            case _:
                pass
            
        request.user.save()
        current_serviceprovider.save()
        print(request.POST.get("is_available"))
    return HttpResponseRedirect('/serviceproviders/serviceproviderprofile')
