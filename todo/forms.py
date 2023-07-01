from django import forms
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Task, Profile


# Register a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Create a task
class CreateTaskForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"rows": "1", "placeholder": "Title..."}),
    )

    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"rows": "3", "placeholder": "Say something..."}),
    )

    class Meta:
        model = Task
        fields = ["title", "content"]
        exclude = ["user"]


# Update a user
class UpdateUserForm(forms.ModelForm):
    password = None

    class Meta:
        model = User
        fields = ["username", "email"]
        exclude = ["password1", "password2"]


# Updata profile picture
class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control-file"})
    )

    class Meta:
        model = Profile
        fields = ["profile_pic"]
