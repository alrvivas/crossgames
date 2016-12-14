from django.db import models
from ejercicios.models import *
from competencias.models import Competencia

class Evento(models.Model):
	competencia = models.ForeignKey(Competencia)
	nombre = models.CharField(max_length=140)
	activo = models.BooleanField(default=False, verbose_name=('Activo'))
	tiempo = models.CharField(max_length=15,null=True, blank=True)		
	repeticiones = models.IntegerField(null=True, blank=True)
	peso = models.DecimalField(max_digits = 12,decimal_places = 4,null=True, blank=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha = models.DateField(null=True,blank=True)
	descripcion = models.TextField(null=True,blank=True)
	imagen = models.ImageField("Imagen Destacada Evento", upload_to="images/eventos", blank=True, null=True,default='images/eventos/default-01.png')
	
	@models.permalink
	def get_absolute_url(self):
		return('evento', (), { 'evento_id': self.id })

	@models.permalink
	def registro_ejercicios_evento(self):
		return('registro-ejercicios-evento', (), { 'evento_id': self.id })

	@models.permalink
	def get_ejercicios(self):
		return('ejercicios-evento', (), { 'evento_id': self.id })

	def __unicode__(self): 
		return unicode(self.nombre)

class Ejercicios_Evento(models.Model):	
	evento = models.ForeignKey(Evento)
	ejercicio = models.ForeignKey(Ejercicio)
	tiempo = models.CharField(max_length=140)
	peso_1 = models.DecimalField(max_digits = 12,decimal_places = 4,null=True, blank=True)
	peso_2 = models.DecimalField(max_digits = 12,decimal_places = 4,null=True, blank=True)
	repeticiones = models.IntegerField(null=True, blank=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self): 
		return unicode(self.id)