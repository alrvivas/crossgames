from django.contrib import admin
from .models import Evento,Ejercicios_Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	list_filter = ('nombre',)
	search_fields = ('nombre',)

@admin.register(Ejercicios_Evento)
class Ejercicios_EventoAdmin(admin.ModelAdmin):
	list_display = ('id','evento','ejercicio')
	list_filter = ('evento',)
	search_fields = ('evento',)