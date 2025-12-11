from django.urls import path
from .views import DashboardView, SignInView, SignOutView, register

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("login/", SignInView.as_view(), name="login"),
    path("register/", register, name="register"),
    path("logout/", SignOutView, name="logout"),
]
