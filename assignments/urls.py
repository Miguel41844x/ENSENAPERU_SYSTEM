from django.urls import path
from . import views

urlpatterns = [
    path("", views.assignment_list, name="assignment_list"),
    path("new/", views.assignment_create, name="assignment_create"),
]
