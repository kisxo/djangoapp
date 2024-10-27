from django.contrib.auth.forms import UserCreationForm
class MyCustomSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    cpf_cnpj = forms.CharField(max_length=14)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'cpf_cnpj', ' first_name', 'last_name', 'password1', 'password2', )