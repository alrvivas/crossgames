from django.db import models

class Equipo(models.Model):
	nombre = models.CharField(max_length=140)
	whatsapp = models.CharField(max_length=15,null=True, blank=True)		
	email = models.CharField(max_length=140,null=True, blank=True)
	ciudad = models.CharField(max_length=140,null=True, blank=True)
	estado = models.CharField(max_length=140,null=True, blank=True)
	imagen = models.ImageField("Logo Equipo", upload_to="images/equipos", blank=True, null=True,default='images/equipos/default-01.png')
	puntos_acumulados = models.DecimalField(max_digits = 12,decimal_places = 4,null=True, blank=True)	
	puntuacion_final = models.DecimalField(max_digits = 12,decimal_places = 4,null=True, blank=True)	

	@models.permalink
	def get_absolute_url(self):
		return('equipo', (), { 'equipo_id': self.id })

	@models.permalink
	def equipo_participantes(self):
		return('equipo-participantes', (), { 'equipo_id': self.id })

	def __unicode__(self): 
		return unicode(self.nombre)