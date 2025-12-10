from django.urls import path
from . import views

urlpatterns = [
    path("schools/", views.school_list, name="school_list"),
    path("schools/new/", views.school_create, name="school_create"),
    path("schools/<int:school_id>/delete/", views.school_delete, name="school_delete"),
    path("agreements/", views.agreement_list, name="agreement_list"),
    path("agreements/<int:agreement_id>/delete/", views.agreement_delete, name="agreement_delete"),
]
