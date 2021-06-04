from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class ImageForm(forms.Form):
    img = forms.ImageField()


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]
