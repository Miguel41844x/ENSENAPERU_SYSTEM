from django import forms

from core.models import ClassSession, Student, StudentEvaluation


class StudentEvaluationForm(forms.ModelForm):
    class Meta:
        model = StudentEvaluation
        fields = [
            "student",
            "session",
            "eval_type",
            "score",
            "comments",
        ]
        widgets = {
            "score": forms.NumberInput(attrs={"step": "0.1"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student"].queryset = Student.objects.order_by("last_name", "first_name")
        self.fields["session"].queryset = ClassSession.objects.select_related("program").order_by("session_date")
