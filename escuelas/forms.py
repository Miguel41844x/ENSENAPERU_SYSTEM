from django import forms

from core.models import Agreement, School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = [
            "name",
            "location",
            "main_contact_name",
            "main_contact_phone",
            "status",
        ]
        labels = {
            "name": "Nombre",
            "location": "Ubicación",
            "main_contact_name": "Contacto principal",
            "main_contact_phone": "Teléfono de contacto",
            "status": "Estado",
        }
        widgets = {"status": forms.Select(choices=[("ACTIVA", "Activa"), ("INACTIVA", "Inactiva")])}


class AgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = [
            "school",
            "status",
            "file_path",
            "start_date",
            "end_date",
        ]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }
