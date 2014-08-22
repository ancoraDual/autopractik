from django.contrib import admin
from .models import Provincia

class ProvinciaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


admin.site.register(Provincia, ProvinciaAdmin)