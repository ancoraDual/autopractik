from django import forms
from django.contrib.auth import authenticate
from .models import Alumno


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellidos', 'email', 'nif', 'direccion', 'poblacion', 'localidad', 'provincia', 'cp', 'autoescuela']

class AlumnoAuthForm(forms.Form):
	
	email = forms.EmailField(label = 'tu email')
	nombre = forms.CharField(max_length= 255, label= 'tu nombre')

	def __init__(self, *args, **kwargs):
		self.usuario = None
		super(AlumnoAuthForm, self).__init__(*args, **kwargs)

	def clean(self):
		email = self.cleaned_data.get('email')
		nombre = self.cleaned_data.get('nombre')

		self.usuario = authenticate(email = email, nombre = nombre)

		if self.usuario is None:
			raise forms.ValidationError('Alumno no autorizado')
		elif not self.usuario.is_active:
			raise forms.ValidationError('Alumno inactivo')

		return self.cleaned_data

	def get_user(self):
		return self.usuario