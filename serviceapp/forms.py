from django import forms
from django.forms import ModelForm
from .models import User
 
# creating a form 
class UserProfileForm(forms.Form):

    password = forms.CharField(widget = forms.PasswordInput())
    contact_phone = forms.CharField(max_length=10)
    address = forms.CharField(max_length=1024)
    zip_code = forms.CharField(max_length=12)
    city = forms.CharField(max_length=1024,)
    is_service_providers = forms.BooleanField()

#create profile form
class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('profile_picture', 'contact_phone', 'address', 'zip_code', 'city')

        labels = {
            'profile_picture': '', 
            'contact_phone': '',
            'address': '',
            'zip_code': '',
            'city': '',     
        }

        widgets = {
            'profile_picture': forms.FileInput( attrs={'class': 'form-control', 'placeholder': 'Upload Profile Picture'}), 
            'contact_phone': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'address': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
            'city': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'City'}) 
        }