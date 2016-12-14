from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'eventos.views.eventos', name='eventos'),
	url(r'^(?P<evento_id>[-\w]+)$', 'eventos.views.evento', name='evento'),
	url(r'^(?P<evento_id>[-\w]+)/registro-ejercicios-evento$', 'eventos.views.registro_ejercicios_evento', name='registro-ejercicios-evento'),
	url(r'^(?P<evento_id>[-\w]+)/ejercicios-evento$', 'eventos.views.ejercicios_evento', name='ejercicios-evento'),
	url(r'^registro-eventos/$', 'eventos.views.registro_eventos', name='registro-eventos'),	
)