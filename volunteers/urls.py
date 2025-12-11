from django.urls import path
from . import views

urlpatterns = [
    path("", views.volunteer_list, name="volunteer_list"),
    path("new/", views.volunteer_create, name="volunteer_create"),
    path("<int:volunteer_id>/delete/", views.volunteer_delete, name="volunteer_delete"),
]
