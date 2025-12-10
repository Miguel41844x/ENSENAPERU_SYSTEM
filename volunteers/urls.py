from django.urls import path
from . import views

urlpatterns = [
    path("", views.volunteer_list, name="volunteer_list"),
    path("new/", views.volunteer_create, name="volunteer_create"),
]
