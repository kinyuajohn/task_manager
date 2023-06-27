from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register),
    path("my-login", views.my_login),
    path("", views.home),
    # CRUD operations
    # CREATE TASK
    path("create-task", views.create_task),
    # READ TASK
    path("view-tasks", views.view_tasks, name="view-tasks"),
]
