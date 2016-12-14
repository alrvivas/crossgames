# -*- coding: utf-8 -*-
from django.db import models

class Configuracion(models.Model):
	nombre = models.CharField(max_length=140)
	whatsapp = models.CharField(max_length=15,null=True, blank=True)		
	email = models.CharField(max_length=140,null=True, blank=True)
	logo = models.ImageField("Logo Aplicación", upload_to="images/configuracion", blank=True, null=True,default='images/configuracion/default-01.png')		

	@models.permalink
	def get_absolute_url(self):
		return('configuracion', (), { 'configuracion_id': self.id })

	def __unicode__(self): 
		return unicode(self.nombre)