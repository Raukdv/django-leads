from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _

from core.models import User

class UserLoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Please enter a correct mail and/or password."
        ),
    }
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    phoneNumber = forms.CharField(max_length=12, required=True, widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    address = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class':'form-control'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phoneNumber', 'address']
