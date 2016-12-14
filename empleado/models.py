from django.db import models
from django.contrib.auth.models import User

class Departamento(models.Model):
	nombre = models.CharField(max_length=140)

	def __unicode__(self): 
		return unicode(self.nombre)

class Empleado(models.Model):
	user = models.OneToOneField(User)
	departamento = models.ForeignKey(Departamento, blank=True, null=True)
	nombre = models.CharField(max_length=140)
	apellidos = models.CharField(max_length=140)
	whatsapp = models.CharField(max_length=15)		
	telefono = models.CharField(max_length=15,null=True, blank=True)

	def __unicode__(self): 
		return unicode(self.user)