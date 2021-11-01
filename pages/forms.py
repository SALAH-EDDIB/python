from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):

    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control", }))

    email = forms.CharField(label='Email',
                            widget=forms.TextInput(attrs={"placeholder": "Email", "class": "form-control", }))

    password1 = forms.CharField(label='password1',
                                widget=forms.TextInput(attrs={"placeholder": "password1", "class": "form-control", }))

    password2 = forms.CharField(label='password2',
                                widget=forms.TextInput(attrs={"placeholder": "password2", "class": "form-control", }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
