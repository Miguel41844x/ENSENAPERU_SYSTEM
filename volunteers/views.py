from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from core.models import Volunteer
from .forms import VolunteerForm


@login_required
def volunteer_list(request):
    search_query = request.GET.get("q", "").strip()
    order_param = request.GET.get("order", "name")

    order_fields = {
        "name": ("last_name", "first_name"),
        "dni": ("dni",),
        "status": ("status", "last_name"),
    }
    ordering = order_fields.get(order_param, order_fields["name"])

    volunteers = Volunteer.objects.all()
    if search_query:
        volunteers = volunteers.filter(
            Q(first_name__icontains=search_query)
            | Q(last_name__icontains=search_query)
            | Q(email__icontains=search_query)
            | Q(dni__icontains=search_query)
        )

    volunteers = volunteers.order_by(*ordering)[:100]
    return render(
        request,
        "volunteers/volunteer_list.html",
        {
            "volunteers": volunteers,
            "search_query": search_query,
            "order_param": order_param if order_param in order_fields else "name",
        },
    )


@login_required
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


@login_required
def volunteer_delete(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)
    if request.method == "POST":
        try:
            volunteer.delete()
            messages.success(request, "Voluntario eliminado correctamente.")
        except IntegrityError:
            messages.error(request, "No se puede eliminar el voluntario porque tiene registros asociados.")
        return redirect("volunteer_list")
