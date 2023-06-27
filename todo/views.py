from django.shortcuts import render

from .models import Task
from .forms import TaskForm

# Create your views here.


def home(request):
    query_single_object = Task.objects.get(id=5)

    context = {"task": query_single_object}

    return render(request, "index.html", context=context)


def register(request):
    return render(request, "register.html")


def my_login(request):
    return render(request, "my-login.html")


def create_task(request):
    form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "task-form.html", context=context)
