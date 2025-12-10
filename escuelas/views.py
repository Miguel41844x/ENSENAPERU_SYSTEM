from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from core.models import Agreement, School
from .forms import SchoolForm


@login_required
def school_list(request):
    schools = School.objects.all().order_by("name")
    return render(request, "schools/school_list.html", {"schools": schools})


@login_required
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


@login_required
def agreement_list(request):
    agreements = Agreement.objects.select_related("school").order_by("-start_date")
    return render(request, "schools/agreement_list.html", {"agreements": agreements})
