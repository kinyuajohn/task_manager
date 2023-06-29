from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm, CreateUserForm, LoginForm

# Create your views here.


def home(request):
    return render(request, "index.html")


# CREATE a task
def create_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("view-tasks")

    context = {
        "form": form,
    }

    return render(request, "create-task.html", context=context)


# READ tasks
def view_tasks(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks,
    }

    return render(request, "view-tasks.html", context=context)


# UPDATE a task
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            return redirect("view-tasks")

    context = {
        "form": form,
    }

    return render(request, "update-task.html", context=context)


# DELETE a task
def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()

        return redirect("view-tasks")

    context = {
        "object": task,
    }

    return render(request, "delete-task.html", context=context)


# Register/create a user
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponse("User registered!")

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
    return render(request, "dashboard.html")


# Logout a user
def user_logout(request):
    auth.logout(request)

    return redirect("")
