from django.db import models
from equipos.models import Equipo

class Participante(models.Model):
	equipo = models.OneToOneField(Equipo)
	nombre = models.CharField(max_length=140)
	apellidos = models.CharField(max_length=140)
	whatsapp = models.CharField(max_length=15,null=True, blank=True)		
	email = models.CharField(max_length=140,null=True, blank=True)
	ciudad = models.CharField(max_length=140,null=True, blank=True)
	estado = models.CharField(max_length=140,null=True, blank=True)
	imagen = models.ImageField("Logo Equipo", upload_to="images/equipos", blank=True, null=True,default='images/equipos/default-01.png')

	@models.permalink
	def get_absolute_url(self):
		return('participante', (), { 'participante_id': self.id })

	def nombre_completo(self):
	    return "%s  %s"% (self.nombre, self.apellidos)

	def __unicode__(self): 
		return unicode(self.nombre)