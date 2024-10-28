from django import forms
from django.forms import ModelForm
from .models import ServiceProviders


class ServiceProfileForm(ModelForm):
    class Meta:
        model = ServiceProviders
        fields = ('contact_email', 'contact_phone', 'service_type', 'bio', 'address', 'zip_code', 'latitude', 'longitude', 'is_available')
        labels = {
            'contact_email': '', 
            'contact_phone': '', 
            'service_type': '', 
            'bio': '', 
            'address': '', 
            'zip_code': '', 
            'latitude': '', 
            'longitude': '', 
            'is_available': '',  
        }

        CHOICES = [
        ('Electrician', 'Electrician'),
        ('Plumber', 'Plumber'),
        ('Carpenter', 'Carpenter'),
        ('Mason', 'Mason'),
        ('Welder', 'Welder'),
        ('Mechanic', 'Mechanic'),
        ('Painter', 'Painter',),
        ('Landscaper', 'Landscaper'),
        ('Pest Control', 'Pest Control')
    ]
        
        # widgets = {
        #     'contact_email': forms.EmailInput( attrs={'class': 'form-control ', 'placeholder': 'Contact Email'}),
        #     'contact_phone': forms.TextInput( attrs={'class': 'form-control ', 'placeholder': 'Contact Phone'}),
        #     'service_type': forms.Select(attrs={'class': 'form-control '},choices=CHOICES),
        #     'bio': forms.TextInput( attrs={'class': 'form-control ', 'placeholder': 'BIO'}),
        #     'address': forms.TextInput( attrs={'class': 'form-control ', 'placeholder': 'Address'}),
        #     'zip_code': forms.TextInput( attrs={'class': 'form-control ', 'placeholder': 'Zip Code'}),
        #     'latitude': forms.FloatField( attrs={'class': 'form-control ', 'placeholder': 'Latitude', 'required': 'required'}, ),
        #     'longitude': forms.FloatField( attrs={'class': 'form-control ', 'placeholder': 'Longitude', 'required': 'required'}, required=True),
        #     'is_available': forms.ChoiceField( attrs={'class': 'form-control ', 'placeholder': 'IS available'}),
        # }