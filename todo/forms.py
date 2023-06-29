from django import forms
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Task


# Register a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Create a task
class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "content",
        ]
        exclude = [
            "user",
        ]
