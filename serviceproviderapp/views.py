from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def serviceproviderhome(request):
    return render(request, "sericeproviderapp/serviceproviderhome.html")