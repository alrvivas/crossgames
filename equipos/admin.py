from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','whatsapp','ciudad','puntos_acumulados','puntuacion_final')
	list_editable = ('puntuacion_final','puntos_acumulados',)
	list_filter = ('nombre','ciudad')
	search_fields = ('nombre',)
