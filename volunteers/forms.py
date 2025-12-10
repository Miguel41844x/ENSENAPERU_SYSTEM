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
        labels = {
            "dni": "DNI",
            "first_name": "Nombres",
            "last_name": "Apellidos",
            "phone": "Teléfono",
            "email": "Correo electrónico",
            "specialty": "Especialidad",
            "status": "Estado",
        }
        widgets = {"status": forms.Select(choices=Volunteer.STATUS_CHOICES)}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["status"].choices = [
            (Volunteer.STATUS_APPLICANT, "Postulante"),
            (Volunteer.STATUS_IN_REVIEW, "En revisión"),
            (Volunteer.STATUS_APPROVED, "Aprobada"),
            (Volunteer.STATUS_REJECTED, "Rechazada"),
            (Volunteer.STATUS_WITHDRAWN, "Retirada"),
        ]
