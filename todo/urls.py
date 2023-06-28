from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register),
    path("my-login/", views.my_login),
    path("", views.home, name=""),
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
    # Login a user
    path("my-login/", views.my_login, name="my-login"),
    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    # Logout a user
    path("user-logout/", views.user_logout, name="user-logout"),
]
