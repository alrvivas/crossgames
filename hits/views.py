# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg,Sum
from .models import *
from equipos.models import *
from eventos.models import *
from hits.models import *
from .forms import *
from django.contrib.auth.models import User
from django.db.models import Q 
from django.forms.models import modelformset_factory

@login_required(login_url='/login/')
def registro_hits(request):
    page_title = "registro de hits"
    user = request.user
    eventos = Evento.objects.all()
    hit = Hit.objects.all()
    if request.method == 'POST':
        form_hit = hitForm(request.POST,request.FILES)
        if form_hit.is_valid():
            hit = form_hit.save(commit = False)
            hit.save()            
            return redirect(hit.registro_equipos_hit())
    else:
        form_hit = hitForm()
    args = {}
    args.update(csrf(request))
    template_name ="registro-hits.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def hits(request):
    page_title = "Hits"
    user = request.user
    hits = Hit.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )    
        results = Hit.objects.filter(qset).order_by('-id')
        template_name = "resultados-hits.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="hits.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

def hit(request,hit_id):
    user = request.user
    hit = get_object_or_404(Hit, id=hit_id)
    equipos = Equipos_Hit.objects.filter(hit=hit).order_by('-puntos')
    page_title = hit.nombre
    template_name ="hit.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def registro_equipos_hit(request,hit_id):
    page_title = "Asignar Equipos"
    user = request.user
    hit = get_object_or_404(Hit, id=hit_id)
    equipos = Equipo.objects.all()
    EquiposHitFormSet = modelformset_factory(Equipos_Hit,form=addequiposForm,extra=len(equipos))
    if request.method == 'POST':
        formset = EquiposHitFormSet(request.POST,request.FILES)
        if formset.is_valid():
            formset.save()            
            return redirect(hit.get_absolute_url())
    else:
        formset = EquiposHitFormSet(queryset=Equipos_Hit.objects.none())
    args = {}
    args.update(csrf(request))
    template_name ="asignar-equipos.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def equipos_hit(request,hit_id):    
    user = request.user
    hit = get_object_or_404(Hit, id=evento_id)
    equipos = Equipos_Hit.objects.filter(hit=hit)  
    page_title = hit.nombre   
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )    
        results = Equipos_Hit.objects.filter(qset,hit=hit).order_by('-id')
        template_name = "equipos-hit-resultado.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []           
    template_name ="equipos-hit.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

def tabla_general(request):    
    user = request.user
    hit = Hit.objects.all()
    equipos = Equipo.objects.all().order_by('-puntuacion_final')
    equipos_hit = Equipos_Hit.objects.all()
    page_title = "Tabla General"                
    template_name ="tabla-general.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 
