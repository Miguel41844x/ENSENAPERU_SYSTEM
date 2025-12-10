from django.contrib import messages
from django.shortcuts import redirect, render

from empresa_educacion.models import Agreement, School
from .forms import SchoolForm


def school_list(request):
    schools = School.objects.all().order_by("name")
    return render(request, "schools/school_list.html", {"schools": schools})


def school_create(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Escuela registrada correctamente.")
            return redirect("school_list")
    else:
        form = SchoolForm()
    return render(request, "schools/school_form.html", {"form": form})


def agreement_list(request):
    agreements = Agreement.objects.select_related("school").order_by("-start_date")
    return render(request, "schools/agreement_list.html", {"agreements": agreements})
