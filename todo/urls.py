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
    # Logout a user
    path("user-logout/", views.user_logout, name="user-logout"),
]
