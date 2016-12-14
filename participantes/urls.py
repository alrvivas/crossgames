from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'participantes.views.participantes', name='participantes'),
	url(r'^(?P<participante_id>[-\w]+)$', 'participantes.views.participante', name='participante'),
	url(r'^registro-participantes/$', 'participantes.views.registro_participantes', name='registro-participantes'),	
)