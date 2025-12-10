from django import forms

from core.models import Agreement, Assignment, Volunteer


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = [
            "volunteer",
            "agreement",
            "start_date",
            "end_date",
            "role",
            "status",
        ]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "status": forms.Select(choices=[("ACTIVO", "Activo"), ("INACTIVO", "Inactivo"), ("FINALIZADO", "Finalizado")]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["volunteer"].queryset = Volunteer.objects.order_by("last_name", "first_name")
        self.fields["agreement"].queryset = Agreement.objects.select_related("school").order_by("school__name")
