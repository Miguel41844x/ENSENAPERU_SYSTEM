from django import forms

from core.models import Volunteer


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            "dni",
            "first_name",
            "last_name",
            "phone",
            "email",
            "specialty",
            "status",
        ]
        widgets = {"status": forms.Select(choices=[("ACTIVO", "Activo"), ("INACTIVO", "Inactivo")])}
