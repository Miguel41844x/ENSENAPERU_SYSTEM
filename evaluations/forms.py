from django import forms

from core.models import AppUser, ClassSession, Student, StudentEvaluation


class StudentEvaluationForm(forms.ModelForm):
    class Meta:
        model = StudentEvaluation
        fields = [
            "stu_eval_id",
            "student",
            "session",
            "eval_type",
            "score",
            "comments",
            "created_by_user",
        ]
        widgets = {
            "score": forms.NumberInput(attrs={"step": "0.1"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student"].queryset = Student.objects.order_by("last_name", "first_name")
        self.fields["session"].queryset = ClassSession.objects.select_related("program").order_by("session_date")
        self.fields["created_by_user"].queryset = AppUser.objects.order_by("username")
