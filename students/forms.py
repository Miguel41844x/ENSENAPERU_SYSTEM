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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["school"].queryset = self.fields["school"].queryset.order_by("name")[:100]
        self.fields["school"].widget.attrs.update(
            {"class": "searchable-select", "data-search": "true"}
        )
