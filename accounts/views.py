from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max
from django.db import DatabaseError, transaction, IntegrityError
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
import logging

from core.models import AppUser, Assignment, School, Student, Volunteer
from .forms import RegistrationForm

logger = logging.getLogger(__name__)

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
            role = data.get("role")
            try:
                with transaction.atomic():
                    # Usuario de Django
                    user_model.objects.create_user(
                        username=data["username"],
                        email=data["email"],
                        password=data["password1"],
                        first_name=data.get("first_name", ""),
                        last_name=data.get("last_name", ""),
                    )

                    last_id = AppUser.objects.aggregate(Max("user_id"))["user_id__max"] or 0
                    new_id = last_id + 1

                    # Usuario en tu tabla APP_USER
                    AppUser.objects.create(
                        user_id=new_id,
                        username=data["username"],
                        password_hash=make_password(data["password1"]),
                        first_name=data.get("first_name", ""),
                        last_name=data.get("last_name", ""),
                        email=data["email"],
                        role=role,
                        active_flag=True,
                    )

                messages.success(request, "Usuario registrado correctamente. Ya puedes iniciar sesión.")
                return redirect("login")

            except IntegrityError as e:
                logger.exception("Error de integridad al registrar usuario")
                form.add_error(None, f"Error de integridad al registrar el usuario: {e}")

            except Exception as e:
                logger.exception("Error inesperado al registrar usuario")
                form.add_error(None, f"Ocurrió un error inesperado: {e}")
    else:
        form = RegistrationForm()

    return render(request, "auth/register.html", {"form": form})

