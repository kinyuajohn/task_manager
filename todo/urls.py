from django.urls import path

from . import views

urlpatterns = [
    # Homepage
    path("", views.home, name=""),
    # Register a user
    path("register/", views.register, name="register"),
    # Login a user
    path("my-login/", views.my_login, name="my-login"),
    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    # Profile management
    path("profile-management/", views.profile_management, name="profile-management"),
    # Delete account
    path("delete-account/", views.delete_account, name="delete-account"),
    # --------------------------------------------------------------------------
    # CRUD OPERATIONS ***
    # CREATE TASK
    path("create-task/", views.create_task, name="create-task"),
    # READ TASKS
    path("view-tasks/", views.view_tasks, name="view-tasks"),
    # UPDATE TASK
    path("update-task/<str:pk>/", views.update_task, name="update-task"),
    # UPDATE TASK
    path("delete-task/<str:pk>/", views.delete_task, name="delete-task"),
    # --------------------------------------------------------------------------
    # Logout a user
    path("user-logout/", views.user_logout, name="user-logout"),
]
