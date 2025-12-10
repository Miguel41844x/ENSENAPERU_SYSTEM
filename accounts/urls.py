from django.urls import path
from .views import DashboardView, SignInView, SignOutView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("login/", SignInView.as_view(), name="login"),
    path("logout/", SignOutView, name="logout"),
]
