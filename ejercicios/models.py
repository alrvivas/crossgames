from django.db import models

class Unidad(models.Model):
	nombre = models.CharField(max_length=140)
	
	def __unicode__(self): 
		return unicode(self.nombre)

class Ejercicio(models.Model):
	nombre = models.CharField(max_length=140)
	dificultad = models.CharField(max_length=140)
	descripcion = models.TextField(null=True,blank=True)		
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	imagen = models.ImageField("Imagen Del Ejercicio", upload_to="images/ejercicios", blank=True, null=True,default='images/ejercicios/default-01.png')
	
	@models.permalink
	def get_absolute_url(self):
		return('ejercicio', (), { 'ejercicio_id': self.id })

	def __unicode__(self): 
		return unicode(self.nombre)