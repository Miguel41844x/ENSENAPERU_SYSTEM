from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Volunteer, School, Student, Assignment, StudentEvaluation, Agreement
from .forms import VolunteerForm, SchoolForm, StudentForm, AssignmentForm, StudentEvaluationForm

@login_required
def dashboard(request):
    stats = {
        "volunteers": Volunteer.objects.count(),
        "schools": School.objects.count(),
        "students": Student.objects.count(),
        "remedial_plans": 0,  # si luego mapeas remedialplan
    }
    return render(request, "dashboard.html", {"stats": stats})

# VOLUNTEERS

@login_required
def volunteer_list(request):
    volunteers = Volunteer.objects.all().order_by("lastname", "firstname")
    return render(request, "volunteers/volunteer_list.html", {"volunteers": volunteers})

@login_required
def volunteer_create(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("volunteer_list")
    else:
        form = VolunteerForm()
    return render(request, "volunteers/volunteer_form.html", {"form": form})

# SCHOOLS / AGREEMENTS

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

# STUDENTS

@login_required
def student_list(request):
    students = Student.objects.select_related("school").all().order_by("lastname")
    return render(request, "students/student_list.html", {"students": students})

@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "students/student_form.html", {"form": form})

# ASSIGNMENTS

@login_required
def assignment_list(request):
    assignments = Assignment.objects.select_related("volunteer", "school").all().order_by("-startdate")
    return render(request, "assignments/assignment_list.html", {"assignments": assignments})

@login_required
def assignment_create(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()  # en producción puedes llamar a spCrearAsignacion vía cursor Oracle
            return redirect("assignment_list")
    else:
        form = AssignmentForm()
        form.fields["volunteer"].queryset = Volunteer.objects.filter(status="Aprobado")
        form.fields["school"].queryset = School.objects.filter(status="Activo")
    return render(request, "assignments/assignment_form.html", {"form": form})

# STUDENT EVALUATIONS

@login_required
def evaluation_list(request):
    evaluations = StudentEvaluation.objects.select_related("student", "session").all().order_by("-evaldate")
    return render(request, "evaluations/evaluation_list.html", {"evaluations": evaluations})

@login_required
def evaluation_create(request):
    if request.method == "POST":
        form = StudentEvaluationForm(request.POST)
        if form.is_valid():
            eval_obj = form.save(commit=False)
            eval_obj.createdbyuser = None  # o mapea request.user → User de Oracle
            eval_obj.save()  # aquí podrías llamar a spRegistrarEvaluacionEstudiante
            return redirect("evaluation_list")
    else:
        form = StudentEvaluationForm()
    return render(request, "evaluations/evaluation_form.html", {"form": form})
