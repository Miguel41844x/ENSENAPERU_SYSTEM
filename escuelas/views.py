from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


"""
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
            return redirect("school_list")
    else:
        form = SchoolForm()
    return render(request, "schools/school_form.html", {"form": form})

@login_required
def agreement_list(request):
    agreements = Agreement.objects.filter(agreementstatus__in=["Firmado", "Activo"]).select_related("school")
    return render(request, "schools/agreement_list.html", {"agreements": agreements})
"""