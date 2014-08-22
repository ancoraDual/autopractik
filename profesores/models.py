from django.db import models
from autoescuelas.models import Autoescuela
from autopractik.models import Provincia

class Profesor(models.Model):
	nombre = models.CharField(max_length=255)
	apellidos = models.CharField(max_length=255, blank=True)
	nif = models.CharField(max_length=255, blank=True)
	email = models.EmailField(max_length=255, blank=True)
	direccion = models.CharField(max_length=255, blank=True)
	poblacion = models.CharField(max_length=255, blank=True)
	localidad = models.CharField(max_length=255, blank=True)
	cp = models.CharField(max_length=5, blank=True)
	provincia = models.ForeignKey(Provincia, null=True)
	foto = models.ImageField(upload_to="profesores/fotos", blank=True)
	autoescuela = models.ForeignKey(Autoescuela, null=True)

	def __unicode__(self):
		return self.nombre