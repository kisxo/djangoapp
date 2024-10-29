from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from .models import ServiceProviders
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas
from serviceapp.models import User
from .models import ServicesOrder

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

        service_provider = ServiceProviders.objects.get(user = id)
        new_order = ServicesOrder(customer = request.user,
                                  customer_name = request.user.username,
                                  customer_latitude = request.POST.get("latitude"),
                                  customer_longitude = request.POST.get("longitude"),
                                  provider = service_provider,
                                  provider_name = f'{service_provider.user.first_name} {service_provider.user.last_name}',
                                  service_time = request.POST.get("service_time")
                                  )
        new_order.save()
        print(type(request.POST.get("service_time")))
        return HttpResponseRedirect('/serviceproviders/customerhistory/')
    
    service_provider = ServiceProviders.objects.get(user = id)

    contex_data = {
        'id': id,
        'service': service_provider,
    }

    return render(request, 'serviceproviderapp/bookservice.html', contex_data)

@login_required
def bulkserviceadd(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/serviceproviders/serviceproviderprofile/')
    if request.method == "POST":
        excel_file = request.FILES['excel_file']

        excel_data_df = pandas.read_excel(excel_file)

        json_str = excel_data_df.to_json()

        print('Excel Sheet to JSON:\n', json_str)

    return render(request, 'serviceproviderapp/bulkserviceadd.html')

@login_required
def searchservice(request):
    
    services = ServiceProviders.objects.all()

    contex_data = {
        'services': services,
    }
    return render(request, 'serviceproviderapp/searchservice.html', contex_data)

@login_required
def customerhistory(request):
    user_orders = ServicesOrder.objects.filter(customer = request.user)

    contex_data = {
        'orders': user_orders
    }

    return render(request, 'serviceproviderapp/customerhistory.html', contex_data)