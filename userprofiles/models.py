from django.db import models
from django.contrib.auth.models import User


class UsuarioAutoescuela(models.Model):
	email = models.CharField(max_length=255)
	user = models.ForeignKey(User)


	def __unicode__(self):
		return self.user.first_name	