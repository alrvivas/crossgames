from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'hits.views.hits', name='hits'),
	url(r'^(?P<hit_id>[-\w]+)$', 'hits.views.hit', name='hit'),
	url(r'^(?P<hit_id>[-\w]+)/registro-equipos-hit$', 'hits.views.registro_equipos_hit', name='registro-equipos-hit'),
	url(r'^(?P<hit_id>[-\w]+)/equipos-hit$', 'hits.views.equipos_hit', name='equipos-hit'),
	url(r'^registro-hits/$', 'hits.views.registro_hits', name='registro-hits'),
	url(r'^tabla-general/$', 'hits.views.tabla_general', name='tabla-general'),		
)