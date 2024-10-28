from django.urls import path
from . import views

app_name = "serviceproviderapp"
urlpatterns = [
    path("accountmode/<slug:option>/", views.accounttype, name="accounttype"),
    path("servicedashboard/", views.servicedashboard, name="servicedashboard"),
    path("serviceproviderprofile/", views.serviceproviderprofile, name="serviceproviderprofile"),
    path("serviceproviderupdate/<slug:field>/", views.serviceproviderupdate, name="serviceproviderupdate"),
    # path("profile", views.profile, name="profile"),
    # path("updateProfile/<slug:field>/", views.updateProfile, name="updateProfile"),
]