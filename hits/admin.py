from django.contrib import admin
from .models import Hit,Equipos_Hit

@admin.register(Hit)
class HitAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','evento')
	list_filter = ('nombre',)
	search_fields = ('nombre',)

@admin.register(Equipos_Hit)
class Equipos_HitAdmin(admin.ModelAdmin):
	list_display = ('id','hit','equipo','tiempo','repeticiones','peso','puntos')
	list_editable = ('tiempo','repeticiones','peso','puntos',)
	list_filter = ('hit','hit__evento',)
	search_fields = ('hit',)