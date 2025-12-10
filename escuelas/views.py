from django.shortcuts import render


def school_list(request):
    return render(request, "schools/school_list.html")


def school_create(request):
    return render(request, "schools/school_form.html")


def agreement_list(request):
    return render(request, "schools/agreement_list.html")
