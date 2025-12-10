from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import DatabaseError
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from empresa_educacion.models import Assignment, School, Student, Volunteer


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


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy("login")
