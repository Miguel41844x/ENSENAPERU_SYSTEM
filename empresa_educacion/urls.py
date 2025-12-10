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
                "company_name": "Enseña Perú",
                "template_title": "Panel de inicio",
                "editable_note": "Favinovech",
            },
        ),
        name="inicio",
    ),
]
