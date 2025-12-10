from django.contrib import messages
from django.shortcuts import redirect, render

from empresa_educacion.models import Assignment
from .forms import AssignmentForm


def assignment_list(request):
    assignments = Assignment.objects.select_related("volunteer", "agreement__school").order_by("-start_date")
    return render(request, "assignments/assignment_list.html", {"assignments": assignments})


def assignment_create(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Asignación creada correctamente.")
            return redirect("assignment_list")
    else:
        form = AssignmentForm()
    return render(request, "assignments/assignment_form.html", {"form": form})
