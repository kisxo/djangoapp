from django.urls import path
from .views import ServicesView

app_name = "apiapp"
urlpatterns = [
    path("services/", ServicesView.as_view(), name='getservicedata'),
]