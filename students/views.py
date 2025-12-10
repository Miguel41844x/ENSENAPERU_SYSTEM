from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from core.models import Student
from .forms import StudentForm


@login_required
def student_list(request):
    search_query = request.GET.get("q", "").strip()
    order_param = request.GET.get("order", "name")

    order_fields = {
        "name": ("last_name", "first_name"),
        "dni": ("dni", "last_name"),
        "school": ("school__name", "last_name"),
    }
    ordering = order_fields.get(order_param, order_fields["name"])

    students = Student.objects.select_related("school")
    if search_query:
        students = students.filter(
            Q(first_name__icontains=search_query)
            | Q(last_name__icontains=search_query)
            | Q(dni__icontains=search_query)
            | Q(student_code__icontains=search_query)
            | Q(school__name__icontains=search_query)
        )

    students = students.order_by(*ordering)[:100]
    return render(
        request,
        "students/student_list.html",
        {
            "students": students,
            "search_query": search_query,
            "order_param": order_param if order_param in order_fields else "name",
        },
    )


@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante registrado correctamente.")
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "students/student_form.html", {"form": form})
