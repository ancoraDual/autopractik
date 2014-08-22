from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('username', 'email')			


class EmailAuthenticationForm(forms.Form):
	email = forms.EmailField(label = 'tu email')
	nombre = forms.CharField(max_length= 255, label= 'tu nombre')

	def __init__(self, *args, **kwargs):
		self.usuario = None
		super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

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


