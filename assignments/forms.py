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
        labels = {
            "volunteer": "Voluntario",
            "agreement": "Convenio",
            "start_date": "Fecha de inicio",
            "end_date": "Fecha de fin",
            "role": "Rol",
            "status": "Estado",
        }
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "status": forms.Select(choices=Assignment.STATUS_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["volunteer"].queryset = Volunteer.objects.order_by("last_name", "first_name")[:100]
        self.fields["agreement"].queryset = (
            Agreement.objects.select_related("school").order_by("school__name")[:100]
        )
        self.fields["status"].choices = [
            (Assignment.STATUS_ACCEPTED, "Aceptada"),
            (Assignment.STATUS_PENDING, "Pendiente"),
        ]
        for field_name in ["volunteer", "agreement"]:
            self.fields[field_name].widget.attrs.update(
                {"class": "searchable-select", "data-search": "true"}
            )
