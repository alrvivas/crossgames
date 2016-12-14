from django.db import models
from eventos.models import Evento
from equipos.models import Equipo
from ejercicios.models import Ejercicio

class Hit(models.Model):
	evento = models.ForeignKey(Evento,null=True,blank=True)
	nombre = models.CharField(max_length=140)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha = models.DateField(null=True,blank=True)
	imagen = models.ImageField("Imagen Hit", upload_to="images/hits", blank=True, null=True,default='images/hits/default-01.png')
	
	@models.permalink
	def get_absolute_url(self):
		return('hit', (), { 'hit_id': self.id })

	@models.permalink
	def registro_equipos_hit(self):
		return('registro-equipos-hit', (), { 'hit_id': self.id })

	@models.permalink
	def get_equipos(self):
		return('equipos-hit', (), { 'hit_id': self.id })

	def __unicode__(self): 
		return unicode(self.nombre)

class Equipos_Hit(models.Model):
	hit = models.ForeignKey(Hit,null=True,blank=True)
	equipo = models.ForeignKey(Equipo)
	tiempo = models.CharField(max_length=140)
	repeticiones = models.IntegerField(null=True, blank=True)
	peso = models.DecimalField(max_digits = 12,decimal_places = 4,null=True, blank=True)
	puntos = models.DecimalField(max_digits = 12,decimal_places = 4,null=True, blank=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)

	def __unicode__(self): 
		return unicode(self.id)
