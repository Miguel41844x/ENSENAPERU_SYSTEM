from django import forms
from .models import Volunteer, School, Student, Assignment, StudentEvaluation

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ["dni", "firstname", "lastname", "phone", "email", "specialty", "experiencetext", "status"]
        widgets = {
            "experiencetext": forms.Textarea(attrs={"rows": 3}),
        }


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ["name", "ubication", "maincontactname", "maincontactphone", "needssummary", "status"]
        widgets = {"needssummary": forms.Textarea(attrs={"rows": 3})}


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["school", "studentcode", "dni", "firstname", "lastname", "birthdate", "grade", "section"]
        widgets = {"birthdate": forms.DateInput(attrs={"type": "date"})}


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["volunteer", "school", "agreement", "startdate", "enddate", "role"]
        widgets = {
            "startdate": forms.DateInput(attrs={"type": "date"}),
            "enddate": forms.DateInput(attrs={"type": "date"}),
        }


class StudentEvaluationForm(forms.ModelForm):
    class Meta:
        model = StudentEvaluation
        fields = ["student", "session", "evaltype", "score", "attendanceflag", "comments"]
        widgets = {
            "score": forms.NumberInput(attrs={"step": "0.1", "min": 0, "max": 20}),
            "comments": forms.Textarea(attrs={"rows": 3}),
        }
