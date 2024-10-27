from django.urls import path
from . import views

app_name = "serviceapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.profile, name="profile"),
    path("updateProfile/<slug:field>/", views.updateProfile, name="updateProfile"),
]