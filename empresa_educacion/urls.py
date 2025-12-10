from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("volunteers/", include("volunteers.urls")),
    path("students/", include("students.urls")),
    path("assignments/", include("assignments.urls")),
    path("evaluations/", include("evaluations.urls")),
    path("escuelas/", include("escuelas.urls")),
]
