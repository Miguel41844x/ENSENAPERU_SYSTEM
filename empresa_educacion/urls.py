from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("login/", auth_views.LoginView.as_view(
        template_name="auth/login.html"
    ), name="login"),

    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    path("", views.dashboard, name="dashboard"),

    path('escuelas/', include('escuelas.urls')),
    path('admin/', admin.site.urls),

    """

    path("volunteers/", views.volunteer_list, name="volunteer_list"),
    path("volunteers/new/", views.volunteer_create, name="volunteer_create"),

    path("students/", views.student_list, name="student_list"),
    path("students/new/", views.student_create, name="student_create"),

    path("assignments/", views.assignment_list, name="assignment_list"),
    path("assignments/new/", views.assignment_create, name="assignment_create"),

    path("evaluations/", views.evaluation_list, name="evaluation_list"),
    path("evaluations/new/", views.evaluation_create, name="evaluation_create"),

    """
    
]
