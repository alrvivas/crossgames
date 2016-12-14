from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'ejercicios.views.ejercicios', name='ejercicios'),
	url(r'^(?P<ejercicio_id>[-\w]+)$', 'ejercicios.views.ejercicio', name='ejercicio'),
	url(r'^registro-ejercicios/$', 'ejercicios.views.registro_ejercicios', name='registro-ejercicios'),	
)