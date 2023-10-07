from  django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegitrationForm(UserCreationForm):
    # Form to create new user
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        ),
    )
    password2 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'email',)
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Username'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email'}
            )
        }



# login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}
        ),
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        ),
    )

