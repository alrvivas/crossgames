from django.db import models

class Competencia(models.Model):
	nombre = models.CharField(max_length=140)
	descripcion = models.TextField(null=True,blank=True)
	ciudad = models.CharField(max_length=140,null=True, blank=True)
	estado = models.CharField(max_length=140,null=True, blank=True)
	fecha_inicio = models.DateField(null=True,blank=True)		
	fecha_terminacion = models.DateField(null=True,blank=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	imagen = models.ImageField("Imagen De La Competencia", upload_to="images/competencias", blank=True, null=True,default='images/competencias/default-01.png')
	
	@models.permalink
	def get_absolute_url(self):
		return('competencia', (), { 'competencia_id': self.id })

	def __unicode__(self): 
		return unicode(self.nombre)