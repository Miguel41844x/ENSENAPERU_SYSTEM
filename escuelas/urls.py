from django.urls import path
from . import views

urlpatterns = [
    path("schools/", views.school_list, name="school_list"),
    path("schools/new/", views.school_create, name="school_create"),
    path("agreements/", views.agreement_list, name="agreement_list")

]