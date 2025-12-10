from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from core.models import Assignment
from .forms import AssignmentForm


@login_required
def assignment_list(request):
    search_query = request.GET.get("q", "").strip()
    order_param = request.GET.get("order", "start_desc")

    order_fields = {
        "start_desc": ("-start_date",),
        "start_asc": ("start_date",),
        "volunteer": ("volunteer__last_name", "volunteer__first_name"),
        "school": ("agreement__school__name", "volunteer__last_name"),
    }
    ordering = order_fields.get(order_param, order_fields["start_desc"])

    assignments = Assignment.objects.select_related("volunteer", "agreement__school")
    if search_query:
        assignments = assignments.filter(
            Q(volunteer__first_name__icontains=search_query)
            | Q(volunteer__last_name__icontains=search_query)
            | Q(agreement__school__name__icontains=search_query)
            | Q(role__icontains=search_query)
            | Q(status__icontains=search_query)
        )

    assignments = assignments.order_by(*ordering)[:100]
    return render(
        request,
        "assignments/assignment_list.html",
        {
            "assignments": assignments,
            "search_query": search_query,
            "order_param": order_param if order_param in order_fields else "start_desc",
        },
    )


@login_required
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
