from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

from .forms import (
    CreateUserForm,
    LoginForm,
    CreateTaskForm,
    UpdateUserForm,
    UpdateProfileForm,
)
from .models import Task, User, Profile

# Create your views here.


def home(request):
    return render(request, "index.html")


# Register/create a user
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            current_user = form.save(commit=False)

            form.save()

            profile = Profile.objects.create(user=current_user)

            messages.success(request, "User registration was successful")

            return redirect("my-login")

    context = {
        "form": form,
    }

    return render(request, "register.html", context=context)


# Login a user
def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {
        "form": form,
    }

    return render(request, "my-login.html", context=context)


# Dashboard
@login_required(login_url="my-login")
def dashboard(request):
    profile_pic = Profile.objects.get(user=request.user)
    context = {
        "profile": profile_pic,
    }

    return render(request, "profile/dashboard.html", context=context)


# Profile management
@login_required(login_url="my-login")
def profile_management(request):
    user_form = UpdateUserForm(instance=request.user)

    profile = Profile.objects.get(user=request.user)

    form_2 = UpdateProfileForm(instance=profile)

    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()

            return redirect("dashboard")

        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if form_2.is_valid():
            form_2.save()

            return redirect("dashboard")

    context = {
        "user_form": user_form,
        "form_2": form_2,
    }

    return render(request, "profile/profile-management.html", context=context)


# Delete account
@login_required(login_url="my-login")
def delete_account(request):
    if request.method == "POST":
        delete_user = User.objects.get(username=request.user)
        delete_user.delete()

        return redirect("")

    return render(request, "profile/delete-account.html")


# CRUD
# Create task
@login_required(login_url="my-login")
def create_task(request):
    form = CreateTaskForm()

    if request.method == "POST":
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.save()

            return redirect("view-tasks")

    context = {
        "form": form,
    }

    return render(request, "profile/create-task.html", context=context)


# View all tasks
@login_required(login_url="my-login")
def view_tasks(request):
    current_user = request.user.id
    tasks = Task.objects.all().filter(user=current_user)

    context = {
        "tasks": tasks,
    }

    return render(request, "profile/view-tasks.html", context=context)


# Update task
@login_required(login_url="my-login")
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTaskForm(instance=task)

    if request.method == "POST":
        form = CreateTaskForm(request.POST, instance=task)

        if form.is_valid:
            form.save()
            return redirect("view-tasks")

    context = {
        "form": form,
    }

    return render(request, "profile/update-task.html", context=context)


# Delete a task
def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()

        return redirect("view-tasks")

    return render(request, "profile/delete-task.html")


# Logout a user
def user_logout(request):
    auth.logout(request)

    return redirect("")
