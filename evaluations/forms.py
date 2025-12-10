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
        labels = {
            "student": "Estudiante",
            "session": "Sesión",
            "eval_type": "Tipo de evaluación",
            "score": "Puntaje",
            "comments": "Comentarios",
        }
        widgets = {
            "score": forms.NumberInput(attrs={"step": "0.1"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student"].queryset = Student.objects.order_by("last_name", "first_name")[:100]
        self.fields["session"].queryset = (
            ClassSession.objects.select_related("program").order_by("session_date")[:100]
        )
        for field_name in ["student", "session"]:
            self.fields[field_name].widget.attrs.update(
                {"class": "searchable-select", "data-search": "true"}
            )
