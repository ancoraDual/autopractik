from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserCreationEmailForm, EmailAuthenticationForm
from django.contrib.auth.models import User
from autoescuelas.models import Autoescuela

def signup (request):
	form = UserCreationEmailForm(request.POST or None)
	
	new_user=User.objects.create_user('sergei', 'sergei@sergei.com', '12345')
	new_user.first_name = 'minombre'
	new_user.last_name = 'mis apellidos'
	new_user.staff = True;
	new_user.save()

	autoescuela = Autoescuela(nombre = 'StopnDrive', user = new_user)
	autoescuela.save()

	if form.is_valid():
		form.save()

	return render(request, 'signup.html', {'form': form})

def signin (request):
	form = EmailAuthenticationForm(request.POST or None)
	
	if form.is_valid():
		login(request, form.get_user())

	return render(request, 'sigin.html', {'form': form})


#@login_required
def bienvenido (request):
 
    if not request.user.is_authenticated():
        return render(request, 'error.html')

	return render(request, 'bienvenido.html')
