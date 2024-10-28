from django.urls import path
from . import views

app_name = "serviceproviderapp"
urlpatterns = [
    path("", views.serviceproviderhome, name="serviceproviderhome"),
    path("serviceproviderprofile/", views.serviceproviderprofile, name="serviceproviderprofile"),
    path("serviceproviderregister/<slug:field>/", views.serviceproviderregister, name="serviceproviderregister"),
    # path("profile", views.profile, name="profile"),
    # path("updateProfile/<slug:field>/", views.updateProfile, name="updateProfile"),
]