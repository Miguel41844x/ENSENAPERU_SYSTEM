"""Rutas principales del proyecto."""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        TemplateView.as_view(
            template_name="base.html",
            extra_context={
                "company_name": "Empresa Educativa",
                "template_title": "Panel de inicio",
                "editable_note": "Personaliza este texto para adaptar la plantilla a tus cursos, instructores y alumnos.",
            },
        ),
        name="inicio",
    ),
]
