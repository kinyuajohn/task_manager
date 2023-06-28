from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register),
    path("my-login/", views.my_login),
    path("", views.home),
    # CRUD operations
    # --------------------------------------------------------------------------
    # CREATE TASK
    path("create-task/", views.create_task, name="create-task"),
    # READ TASK
    path("view-tasks/", views.view_tasks, name="view-tasks"),
    # UPDATE TASK
    path("update-task/<str:pk>/", views.update_task, name="update-task"),
    # DELETE TASK
    path("delete-task/<str:pk>/", views.delete_task, name="delete-task"),
    # --------------------------------------------------------------------------
    # Register a user
    path("register/", views.register, name="register"),
]
