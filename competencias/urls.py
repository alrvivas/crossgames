from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'competencias.views.competencias', name='competencias'),
	url(r'^(?P<competencia_id>[-\w]+)$', 'competencias.views.competencia', name='competencia'),
	#url(r'^(?P<evento_id>[-\w]+)/registro-ejercicios-evento$', 'competencias.views.registro_ejercicios_evento', name='registro-ejercicios-evento'),
	#url(r'^(?P<evento_id>[-\w]+)/ejercicios-evento$', 'competencias.views.ejercicios_evento', name='ejercicios-evento'),
	url(r'^registro-competencias/$', 'competencias.views.registro_competencias', name='registro-competencias'),	
)