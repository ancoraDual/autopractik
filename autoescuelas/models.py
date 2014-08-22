from django.db import models
from django.contrib.auth.models import User

class Autoescuela(models.Model):
	nombre = models.CharField(max_length=255)
	cif = models.CharField(max_length=255)
	direccion = models.TextField(blank = True)
	logo = models.ImageField(upload_to="autoescuelas/logos")
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre	

class TipoVehiculo(models.Model):
	nombre = models.CharField(max_length=255)

	def __unicode__(self):
		return self.nombre	

class Vehiculo(models.Model):
	nombre = models.CharField(max_length=255)
	matricula = models.CharField(max_length=255)
	foto = models.ImageField(upload_to="autoescuelas/vehiculos")
	autoescuela = models.ForeignKey(Autoescuela, null = True)
	tipovehiculo = models.ForeignKey(TipoVehiculo, default=1)
	duracion = models.IntegerField()


	def __unicode__(self):
		return self.nombre	

from alumnos.models import Alumno

class EstadoSaldo(models.Model):
	nombre = models.CharField(max_length=255)

	def __unicode__(self):
		return self.nombre

class Saldo(models.Model):
	fecha = models.DateTimeField(auto_now=True)
	importe = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	concepto = models.CharField(max_length=255)
	comentarios = models.TextField(blank=True)
	autoescuela = models.ForeignKey(Autoescuela, null = True)
	alumno = models.ForeignKey(Alumno)
	estado = models.ForeignKey(EstadoSaldo, default=2)

	def __unicode__(self):
		return self.concepto

class Practica(models.Model):
	fecha = models.DateTimeField()
	duracion = models.IntegerField()
	importe = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	
	cancelada = models.BooleanField(default=False)
	fecha_cancelacion = models.DateTimeField(blank=True, null=True)
	importe_cancelacion = models.DecimalField(max_digits=7, decimal_places=2, default=0)

	alumno = models.ForeignKey(Alumno)
	vehiculo = models.ForeignKey(Vehiculo)

	def __unicode__(self):
		return self.alumno.nombre

class Calendario(models.Model):
	nombre = models.CharField(max_length=255)
	inicio = models.DateTimeField()
	fin = models.DateTimeField()

	def __unicode__(self):
		return self.nombre

class Horario(models.Model):
	hora = models.TimeField()
	importe_lunes = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	importe_martes = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	importe_miercoles = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	importe_jueves = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	importe_viernes = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	importe_sabado = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	importe_domingo = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	tipovehiculo = models.ForeignKey(TipoVehiculo)
	autoescuela = models.ForeignKey(Autoescuela)
	calendario = models.ForeignKey(Calendario)

	def __unicode__(self):
		return unicode(self.hora)



	









