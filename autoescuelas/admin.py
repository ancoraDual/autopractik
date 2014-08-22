from django.contrib import admin
from .models import *

class AutoescuelaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'cif', 'direccion')

class TipoVehiculoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

class VehiculoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'matricula', 'duracion', 'tipovehiculo', 'autoescuela')

class SaldoAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'concepto', 'importe', 'estado', 'alumno', 'autoescuela')

class EstadoSaldoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

class PracticaAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'alumno', 'vehiculo', 'cancelada')

class CalendarioAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'inicio', 'fin')

class HorarioAdmin(admin.ModelAdmin):
	list_display = ('autoescuela', 'calendario', 'tipovehiculo', 'hora', 'importe_lunes')


admin.site.register(Autoescuela, AutoescuelaAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Saldo, SaldoAdmin)
admin.site.register(EstadoSaldo, EstadoSaldoAdmin)
admin.site.register(Practica, PracticaAdmin)
admin.site.register(TipoVehiculo, TipoVehiculoAdmin)
admin.site.register(Calendario, CalendarioAdmin)
admin.site.register(Horario, HorarioAdmin)

