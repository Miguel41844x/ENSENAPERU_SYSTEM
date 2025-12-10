from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import DatabaseError, transaction
from django.views.generic import TemplateView
from django.shortcuts import redirect, render

from core.models import AppUser, Assignment, School, Student, Volunteer
from .forms import RegistrationForm


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        counts = {
            "volunteers": 0,
            "schools": 0,
            "students": 0,
            "assignments": 0,
        }
        try:
            counts["volunteers"] = Volunteer.objects.count()
            counts["schools"] = School.objects.count()
            counts["students"] = Student.objects.count()
            counts["assignments"] = Assignment.objects.count()
        except DatabaseError:
            # En entornos sin base de datos disponible simplemente dejamos los valores en cero
            pass
        context.update(counts)
        return context


class SignInView(auth_views.LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True


def SignOutView(request):
    logout(request)
    return redirect("login")


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_model = get_user_model()
            try:
                with transaction.atomic():
                    user_model.objects.create_user(
                        username=data["username"],
                        email=data["email"],
                        password=data["password1"],
                        first_name=data.get("first_name", ""),
                        last_name=data.get("last_name", ""),
                    )
                    AppUser.objects.create(
                        username=data["username"],
                        password_hash=make_password(data["password1"]),
                        first_name=data.get("first_name", ""),
                        last_name=data.get("last_name", ""),
                        email=data["email"],
                        role=data["role"],
                        active_flag=True,
                    )
                messages.success(request, "Usuario registrado correctamente. Ya puedes iniciar sesión.")
                return redirect("login")
            except Exception:
                form.add_error(None, "Ocurrió un error al registrar el usuario. Inténtalo nuevamente.")
    else:
        form = RegistrationForm()

    return render(request, "auth/register.html", {"form": form})

