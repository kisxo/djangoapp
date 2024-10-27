from django import forms
 
# creating a form 
class UserProfileForm(forms.Form):

    password = forms.CharField(widget = forms.PasswordInput())
    contact_phone = forms.CharField(max_length=10)
    address = forms.CharField(max_length=1024)
    zip_code = forms.CharField(max_length=12)
    city = forms.CharField(max_length=1024,)
    is_service_providers = forms.BooleanField()
