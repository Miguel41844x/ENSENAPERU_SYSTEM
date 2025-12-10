from django import forms

from core.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "school",
            "student_code",
            "dni",
            "first_name",
            "last_name",
            "birthdate",
        ]
        widgets = {"birthdate": forms.DateInput(attrs={"type": "date"})}
