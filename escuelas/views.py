from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from core.models import Agreement, School
from .forms import SchoolForm


@login_required
def school_list(request):
    search_query = request.GET.get("q", "").strip()
    order_param = request.GET.get("order", "name")

    order_fields = {
        "name": ("name",),
        "location": ("location", "name"),
        "status": ("status", "name"),
    }
    ordering = order_fields.get(order_param, order_fields["name"])

    schools = School.objects.all()
    if search_query:
        schools = schools.filter(
            Q(name__icontains=search_query)
            | Q(location__icontains=search_query)
            | Q(main_contact_name__icontains=search_query)
            | Q(main_contact_phone__icontains=search_query)
        )

    schools = schools.order_by(*ordering)[:100]
    return render(
        request,
        "schools/school_list.html",
        {
            "schools": schools,
            "search_query": search_query,
            "order_param": order_param if order_param in order_fields else "name",
        },
    )


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
    search_query = request.GET.get("q", "").strip()
    order_param = request.GET.get("order", "start_desc")

    order_fields = {
        "start_desc": ("-start_date", "-agreement_id"),
        "start_asc": ("start_date", "agreement_id"),
        "school": ("school__name", "-start_date"),
        "status": ("status", "-start_date"),
    }
    ordering = order_fields.get(order_param, order_fields["start_desc"])

    agreements = Agreement.objects.select_related("school")
    if search_query:
        agreements = agreements.filter(
            Q(school__name__icontains=search_query)
            | Q(status__icontains=search_query)
            | Q(file_path__icontains=search_query)
        )

    agreements = agreements.order_by(*ordering)[:100]
    return render(
        request,
        "schools/agreement_list.html",
        {
            "agreements": agreements,
            "search_query": search_query,
            "order_param": order_param if order_param in order_fields else "start_desc",
        },
    )


@login_required
def school_delete(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    if request.method == "POST":
        try:
            school.delete()
            messages.success(request, "Escuela eliminada correctamente.")
        except IntegrityError:
            messages.error(request, "No se puede eliminar la escuela porque tiene registros asociados.")
        return redirect("school_list")


@login_required
def agreement_delete(request, agreement_id):
    agreement = get_object_or_404(Agreement, pk=agreement_id)
    if request.method == "POST":
        try:
            agreement.delete()
            messages.success(request, "Convenio eliminado correctamente.")
        except IntegrityError:
            messages.error(request, "No se puede eliminar el convenio porque está vinculado a otros registros.")
        return redirect("agreement_list")
