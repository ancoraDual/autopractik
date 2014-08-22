from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core import serializers
from django.core.mail import send_mail
from django.utils import simplejson

from .forms import *
from .models import *

from alumnos.models import Alumno
from alumnos.forms import AlumnoForm
from autopractik.models import Provincia

from profesores.models import Profesor
from profesores.forms import ProfesorForm


def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))

def logIn(request):
	form = logInForm(request.POST or None)
	
	if form.is_valid():
		login(request, form.get_user())
		return HttpResponseRedirect('/autoescuelas/dashboard/')
	

	return render(request, 'login.html', {'form': form})

def logOut(request):
	logout(request)
	return HttpResponseRedirect("/autoescuelas")

# = Secciones principales
# --------------------------

@login_required(login_url='/autoescuelas/')
def dashboard(request):
	return render(request, 'autoescuelas_dashboard.html')

@login_required(login_url='/autoescuelas/')
def reservas(request):
	return render(request, 'autoescuelas_reservas.html')



@login_required(login_url='/autoescuelas/')
def perfil(request):
	return render(request, 'autoescuelas_perfil.html')


# = Alumnos
# --------------

@login_required(login_url='/autoescuelas/')
def alumnos(request):

	search = request.GET.get("search")
	
	#import ipdb; ipdb.set_trace()	

	if search is None:
		alumnos = Alumno.objects.all().order_by('-apellidos')
	else:
		alumnos = Alumno.objects.filter(nombre__contains = search).order_by('-apellidos')

	return render(request, 'autoescuelas_alumnos.html', {"alumnos": alumnos})

@login_required
def alumnos_edit(request, id):
	
	print "id"
	print id


	if id == "0":
		alumno = Alumno()
	else:
		alumno = Alumno.objects.get(pk = id)

	provincias = Provincia.objects.all()

	return render(request, 'estructura/alumno_form.html', { "alumno": alumno, "provincias": provincias})

@login_required
def alumnos_save(request, id):


	print request.POST

	if request.method == "POST":
		
		provincia = Provincia.objects.get(pk = request.POST.get("provincia"))
		autoescuela = Autoescuela.objects.get(pk = 2)

		if id == "0":

			form = AlumnoForm(request.POST)
			form.save()
			
		else:

			alumno = Alumno.objects.get( pk = id )
			alumno = AlumnoForm(request.POST, instance= alumno)
			alumno.save()

		# actualizando
		# autoescuela = Autoescuela.objects.get( pk = request.POST.get('pk') )
		# AutoForm = AutoescuelaForm(request.POST, instance = autoescuela)
		# AutoForm.save()

		# insertando
		# user = User.objects.get(id=2)
		# autoescuela = Autoescuela(nombre= request.POST.get('nombre'), user = user)
		# autoescuela.save()

		# autoescuela = Autoescuela.objects.get( pk = request.POST.get('id') )
		# autoescuela.nombre = request.POST.get('nombre')
		# autoescuela.save()
 		
 		return HttpResponse('Success')

# = Profesores
# --------------

@login_required(login_url='/autoescuelas/')
def profesores(request):

	search = request.GET.get("search")
	
	if search is None:
		profesores = Profesor.objects.all().order_by('-apellidos')
	else:
		profesores = Profesor.objects.filter(nombre__contains = search).order_by('-apellidos')

	return render(request, 'autoescuelas_profesores.html', {"profesores": profesores})
	
@login_required
def profesores_edit(request, id):
	
	if id == "0":
		profesor = Profesor()
	else:
		profesor = Profesor.objects.get(pk = id)

	provincias = Provincia.objects.all()

	return render(request, 'estructura/profesor_form.html', { "profesor": profesor, "provincias": provincias})

@login_required
def profesores_save(request, id):

	if request.method == "POST":
		
		provincia = Provincia.objects.get(pk = request.POST.get("provincia"))
		autoescuela = Autoescuela.objects.get(pk = 2)

		if id == "0":

			form = ProfesorForm(request.POST)
			form.save()
			
		else:

			profesor = Profesor.objects.get( pk = id )
			profesor = ProfesorForm(request.POST, instance= profesor)
			profesor.save()

 		return HttpResponse('Success')


# = Vehiculo
# --------------

@login_required(login_url='/autoescuelas/')
def vehiculos(request):

	search = request.GET.get("search")
	
	if search is None:
		vehiculos = Vehiculo.objects.all().order_by('-nombre')
	else:
		vehiculos = Vehiculo.objects.filter(nombre__contains = search).order_by('-nombre')

	return render(request, 'autoescuelas_vehiculos.html', {"vehiculos": vehiculos})
	
@login_required
def vehiculos_edit(request, id):
	
	tiposvehiculo = TipoVehiculo.objects.all().order_by("id")

	if id == "0":
		vehiculo = Vehiculo()
	else:
		vehiculo = Vehiculo.objects.get(pk = id)

	return render(request, 'estructura/vehiculo_form.html', { "vehiculo": vehiculo, "tiposvehiculo" : tiposvehiculo})

@login_required
def vehiculos_save(request, id):

	if request.method == "POST":
		
		autoescuela = Autoescuela.objects.get(pk = 2)

		if id == "0":

			form = VehiculoForm(request.POST)
			form.save()
			
		else:

			vehiculo = Vehiculo.objects.get( pk = id )
			vehiculo = VehiculoForm(request.POST, instance= vehiculo)
			vehiculo.save()

 		return HttpResponse('Success')


# = Practicas
# --------------

@login_required(login_url='/autoescuelas/')
def practicas(request):

	practicas = Practica.objects.all().order_by('-fecha')
	vehiculos = Vehiculo.objects.all().order_by('nombre')

	return render(request, 'autoescuelas_practicas.html', {"practicas": practicas, "vehiculos": vehiculos})

@login_required
def practicas_edit(request, id):
	
	alumnos = Alumno.objects.all().order_by('apellidos')
	vehiculos = Vehiculo.objects.all().order_by('nombre')
	
	if id == "0":
		practica = Practica()
	else:
		practica = Practica.objects.get(pk = id)

	return render(request, 'estructura/practica_form.html', { "practica": practica, "alumnos": alumnos, "vehiculos": vehiculos})


@login_required
def practicas_save(request, id):

	if request.method == "POST":
		
		autoescuela = Autoescuela.objects.get(pk = 2)

		if id == "0":

			form = PracticaForm(request.POST)
			form.save()
		else:

			practica = Practica.objects.get( pk = id )
			practica = PracticaForm(request.POST, instance= practica)
			practica.save()

 		return HttpResponse('Success')

# = Horarios
# --------------

@login_required(login_url='/autoescuelas/')
def horarios(request):
	
	tiposvehiculo = TipoVehiculo.objects.all().order_by("id")
	horarios = Horario.objects.all().order_by("hora")
	calendarios = Calendario.objects.all().order_by("inicio")

	return render(request, 'autoescuelas_horarios.html', {"tiposvehiculo": tiposvehiculo, "horarios" : horarios, "calendarios" : calendarios, "tiposvehiculo" : tiposvehiculo})

@login_required
def horarios_edit(request, id):
	
	alumnos = Alumno.objects.all().order_by('apellidos')
	vehiculos = Vehiculo.objects.all().order_by('nombre')
	
	if id == "0":
		horarios = Horario()
	else:
		horarios = Horario.objects.get(pk = id)

	return render(request, 'estructura/horario_form.html', { "horarios": horarios, "alumnos": alumnos, "vehiculos": vehiculos})


@login_required
def horarios_save(request, id):


	if request.method == "POST":
		
		if id == "0":

			form = HorarioForm(request.POST)
			form.save()
			
		else:

			horario = Horario.objects.get( pk = id )
			horario = HorarioForm(request.POST, instance= horario)
			horario.save()

 		return HttpResponse('Success')

# = Saldo
# --------------

@login_required(login_url='/autoescuelas/')
def saldos(request):

	search = request.GET.get("search")
	
	#import ipdb; ipdb.set_trace()	

	if search is None:
		saldos = Saldo.objects.all().order_by('-fecha')
	else:
		saldos = Saldo.objects.filter(concepto__contains = search).order_by('-fecha')

	return render(request, 'autoescuelas_saldo.html', {"saldos": saldos})

@login_required
def saldos_edit(request, id):
	
	alumnos = Alumno.objects.all().order_by('apellidos')
	estados = EstadoSaldo.objects.all().order_by('nombre')
	
	if id == "0":
		saldo = Saldo()
	else:
		saldo = Saldo.objects.get(pk = id)

	return render(request, 'estructura/saldo_form.html', { "saldo": saldo, "alumnos": alumnos, "estados": estados})


@login_required
def saldos_save(request, id):

	if request.method == "POST":
		
		autoescuela = Autoescuela.objects.get(pk = 2)

		if id == "0":

			form = SaldoForm(request.POST)
			form.save()
			send_mail("Asunto del mensaje", "Cuerpo del mensaje 6", "sergi@ancoradual.com", ['martin@ancoradual.com'])
		else:

			saldo = Saldo.objects.get( pk = id )
			saldo = SaldoForm(request.POST, instance= saldo)
			saldo.save()

 		return HttpResponse('Success')


# = Old
# ------------------

@login_required
def alumnos_getallhtml(request):

	autoescuelas = Autoescuela.objects.all()
	json = serializers.serialize('json', autoescuelas)

	return render(request, 'alumnos_getall.html', {'json': json, 'autoescuelas': autoescuelas})

@login_required
def alumnos_getalljson(request):

	autoescuelas = Autoescuela.objects.all()
	json = serializers.serialize('json', autoescuelas)

	return HttpResponse(simplejson.dumps(json), mimetype='application/json')






