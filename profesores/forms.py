from django import forms
from django.contrib.auth import authenticate
from .models import Profesor


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellidos', 'email', 'nif', 'direccion', 'poblacion', 'localidad', 'provincia', 'cp', 'autoescuela']
