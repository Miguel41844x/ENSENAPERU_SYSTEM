from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from core.models import AppUser, StudentEvaluation
from .forms import StudentEvaluationForm


@login_required
def evaluation_list(request):
    search_query = request.GET.get("q", "").strip()
    order_param = request.GET.get("order", "recent")

    order_fields = {
        "recent": ("-stu_eval_id",),
        "score": ("-score", "-stu_eval_id"),
        "student": ("student__last_name", "student__first_name"),
    }
    ordering = order_fields.get(order_param, order_fields["recent"])

    evaluations = StudentEvaluation.objects.select_related(
        "student__school",
        "session__program",
        "created_by_user",
    )
    if search_query:
        evaluations = evaluations.filter(
            Q(student__first_name__icontains=search_query)
            | Q(student__last_name__icontains=search_query)
            | Q(eval_type__icontains=search_query)
            | Q(created_by_user__username__icontains=search_query)
        )

    evaluations = evaluations.order_by(*ordering)[:100]
    return render(
        request,
        "evaluations/evaluation_list.html",
        {
            "evaluations": evaluations,
            "search_query": search_query,
            "order_param": order_param if order_param in order_fields else "recent",
        },
    )


@login_required
def evaluation_create(request):
    if request.method == "POST":
        form = StudentEvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.created_by_user = AppUser.objects.filter(username=request.user.username).first()
            evaluation.save()
            messages.success(request, "Evaluación registrada correctamente.")
            return redirect("evaluation_list")
    else:
        form = StudentEvaluationForm()
    return render(request, "evaluations/evaluation_form.html", {"form": form})
