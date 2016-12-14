from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'equipos.views.equipos', name='equipos'),
	url(r'^(?P<equipo_id>[-\w]+)$', 'equipos.views.equipo', name='equipo'),
	url(r'^(?P<equipo_id>[-\w]+)/participantes$', 'equipos.views.equipo_participantes', name='equipo-participantes'),
	url(r'^registro-equipo/$', 'equipos.views.registro_equipo', name='registro-equipo'),	
)