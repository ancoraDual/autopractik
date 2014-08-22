from django.contrib import admin
from .models import Profesor


class ProfesorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellidos', 'email', 'nif', 'autoescuela')

admin.site.register(Profesor, ProfesorAdmin)