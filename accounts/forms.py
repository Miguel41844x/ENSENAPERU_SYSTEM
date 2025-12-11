from django import forms
from django.contrib.auth import get_user_model

from core.models import AppUser


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, label="Usuario")
    email = forms.EmailField(label="Correo electrónico")
    first_name = forms.CharField(max_length=50, label="Nombre", required=False)
    last_name = forms.CharField(max_length=50, label="Apellidos", required=False)
    role = forms.CharField(max_length=20, label="Rol")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        user_model = get_user_model()
        if user_model.objects.filter(username=username).exists() or AppUser.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya está en uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        user_model = get_user_model()
        if user_model.objects.filter(email=email).exists() or AppUser.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está registrado.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Las contraseñas no coinciden.")
        return cleaned_data
