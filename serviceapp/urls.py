from django.urls import path
from . import views

app_name = "serviceapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("updateProfile", views.updateProfile, name="updateProfile"),
]