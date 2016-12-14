from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
   	url(r'^$', 'empleado.views.index', name='index'), 
    url(r'^login/$', 'empleado.views.LoginView', name='login'),
    url(r'^logout/$', 'empleado.views.LogoutView', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^competencias/', include('competencias.urls')),    
    url(r'^equipos/', include('equipos.urls')),
    url(r'^participantes/', include('participantes.urls')),
    url(r'^ejercicios/', include('ejercicios.urls')),
    url(r'^eventos/', include('eventos.urls')),
    url(r'^hits/', include('hits.urls')),
)
handler404 = 'productos.views.file_not_found_404' 
if settings.DEBUG == False:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
   )