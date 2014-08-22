from django.contrib import admin
from .models import Foto, Alumno

class FotoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'foto')

admin.site.register(Foto, FotoAdmin)


class AlumnoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellidos', 'email', 'nif', 'autoescuela')

admin.site.register(Alumno, AlumnoAdmin)

