from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from core.models import StudentEvaluation
from .forms import StudentEvaluationForm


@login_required
def evaluation_list(request):
    evaluations = (
        StudentEvaluation.objects.select_related(
            "student__school",
            "session__program",
            "created_by_user",
        ).order_by("-stu_eval_id")
    )
    return render(request, "evaluations/evaluation_list.html", {"evaluations": evaluations})


@login_required
def evaluation_create(request):
    if request.method == "POST":
        form = StudentEvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Evaluación registrada correctamente.")
            return redirect("evaluation_list")
    else:
        form = StudentEvaluationForm()
    return render(request, "evaluations/evaluation_form.html", {"form": form})
