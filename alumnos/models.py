from django.db import models
from django.contrib.auth.models import User
from autoescuelas.models import Autoescuela
from autopractik.models import Provincia

class Foto(models.Model):
	nombre = models.CharField(max_length=255)
	foto = models.ImageField(upload_to="alumnos/fotos")
	autoescuela = models.ForeignKey(Autoescuela)

	def __unicode__(self):
		return self.nombre	


class Alumno(models.Model):
	nombre = models.CharField(max_length=255)
	apellidos = models.CharField(max_length=255, blank=True)
	nif = models.CharField(max_length=255, blank=True)
	email = models.EmailField(max_length=255, blank=True)
	direccion = models.CharField(max_length=255, blank=True)
	poblacion = models.CharField(max_length=255, blank=True)
	localidad = models.CharField(max_length=255, blank=True)
	cp = models.CharField(max_length=5, blank=True)
	provincia = models.ForeignKey(Provincia, null=True)
	foto = models.ImageField(upload_to="alumnos/fotos", blank=True)
	autoescuela = models.ForeignKey(Autoescuela, null=True)

	def __unicode__(self):
		return self.nombre
