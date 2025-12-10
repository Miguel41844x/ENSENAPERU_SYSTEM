from django.contrib import messages
from django.shortcuts import redirect, render

from core.models import Volunteer
from .forms import VolunteerForm


def volunteer_list(request):
    volunteers = Volunteer.objects.all().order_by("last_name", "first_name")
    return render(request, "volunteers/volunteer_list.html", {"volunteers": volunteers})


def volunteer_create(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Voluntario registrado correctamente.")
            return redirect("volunteer_list")
    else:
        form = VolunteerForm()
    return render(request, "volunteers/volunteer_form.html", {"form": form})
