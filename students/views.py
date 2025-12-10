from django.contrib import messages
from django.shortcuts import redirect, render

from core.models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.select_related("school").order_by("last_name", "first_name")
    return render(request, "students/student_list.html", {"students": students})


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
