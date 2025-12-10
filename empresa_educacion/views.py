from django.shortcuts import render


def dashboard(request):
    return render(request, "dashboard.html")


def simple_login(request):
    return render(request, "auth/login.html")


def simple_logout(request):
    return render(request, "auth/login.html")


def volunteer_list(request):
    return render(request, "volunteers/volunteer_list.html")


def volunteer_create(request):
    return render(request, "volunteers/volunteer_form.html")


def student_list(request):
    return render(request, "students/student_list.html")


def student_create(request):
    return render(request, "students/student_form.html")


def assignment_list(request):
    return render(request, "assignments/assignment_list.html")


def assignment_create(request):
    return render(request, "assignments/assignment_form.html")


def evaluation_list(request):
    return render(request, "evaluations/evaluation_list.html")


def evaluation_create(request):
    return render(request, "evaluations/evaluation_form.html")
