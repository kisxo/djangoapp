from django.urls import path
from . import views

app_name = "serviceprovider"
urlpatterns = [
    path("", views.serviceproviderhome, name="serviceproviderhome"),
    # path("profile", views.profile, name="profile"),
    # path("updateProfile/<slug:field>/", views.updateProfile, name="updateProfile"),
]