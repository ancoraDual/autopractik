from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Autoescuela, Vehiculo, Saldo, Practica, Horario

class AutoescuelaForm(forms.ModelForm):
    class Meta:
        model = Autoescuela
        fields = ['nombre', 'direccion', 'cif']


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['nombre', 'matricula', 'tipovehiculo', 'duracion']


class SaldoForm(forms.ModelForm):
    class Meta:
        model = Saldo
        fields = ['importe', 'concepto', 'comentarios', 'estado', 'alumno', 'autoescuela']

class PracticaForm(forms.ModelForm):
    class Meta:
        model = Practica
        fields = ['fecha', 'duracion', 'importe', 'vehiculo', 'alumno']


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['hora', 'tipovehiculo', 'calendario', 'autoescuela', 'importe_lunes', 'importe_martes', 'importe_miercoles', 'importe_jueves', 'importe_viernes', 'importe_sabado', 'importe_domingo']

# Old       


class logInForm(forms.Form):
	email = forms.EmailField(label = 'tu email')
	nombre = forms.CharField(max_length= 255, label= 'tu nombre')

	def __init__(self, *args, **kwargs):
		self.usuario = None
		super(logInForm, self).__init__(*args, **kwargs)

	def clean(self):
		email = self.cleaned_data.get('email')
		nombre = self.cleaned_data.get('nombre')

		self.usuario = authenticate(email = email, nombre = nombre)

		if self.usuario is None:
			raise forms.ValidationError('Usuario no autorizado')
		elif not self.usuario.is_active:
			raise forms.ValidationError('Usuario inactivo')

		return self.cleaned_data

	def get_user(self):
		return self.usuario