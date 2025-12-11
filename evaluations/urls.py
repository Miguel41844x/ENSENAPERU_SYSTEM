from django.urls import path
from . import views

urlpatterns = [
    path("", views.evaluation_list, name="evaluation_list"),
    path("new/", views.evaluation_create, name="evaluation_create"),
    path("<int:evaluation_id>/delete/", views.evaluation_delete, name="evaluation_delete"),
]
