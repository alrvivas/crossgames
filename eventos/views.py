# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg,Sum
from .models import *
from ejercicios.models import *
from hits.models import *
from .forms import *
from django.contrib.auth.models import User
from django.db.models import Q 
from django.forms.models import modelformset_factory

@login_required(login_url='/login/')
def registro_eventos(request):
    page_title = "registro de eventos"
    user = request.user
    evento = Evento.objects.all()
    if request.method == 'POST':
        form_evento = eventoForm(request.POST,request.FILES)
        if form_evento.is_valid():
            evento = form_evento.save(commit = False)
            evento.save()            
            return redirect(evento.registro_ejercicios_evento())
    else:
        form_evento = eventoForm()
    args = {}
    args.update(csrf(request))
    template_name ="registro-eventos.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def eventos(request):
    page_title = "Eventos"
    user = request.user
    eventos = Evento.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )    
        results = Evento.objects.filter(qset).order_by('-id')
        template_name = "resultados-eventos.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="eventos.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

def evento(request,evento_id):
    user = request.user
    evento = get_object_or_404(Evento, id=evento_id)
    ejercicios = Ejercicios_Evento.objects.filter(evento=evento)
    hits = Hit.objects.filter(evento=evento)
    page_title = evento.nombre
    template_name ="evento.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def registro_ejercicios_evento(request,evento_id):
    page_title = "Asignar Ejercicios"
    user = request.user
    evento = get_object_or_404(Evento, id=evento_id)
    ejercicios = Ejercicio.objects.all()
    EjerciciosEventoFormSet = modelformset_factory(Ejercicios_Evento,form=addejericiciosForm,extra=len(ejercicios))
    if request.method == 'POST':
        formset = EjerciciosEventoFormSet(request.POST,request.FILES)
        if formset.is_valid():
            formset.save()            
            return redirect(evento.get_absolute_url())
    else:
        formset = EjerciciosEventoFormSet(queryset=Ejercicios_Evento.objects.none())
    args = {}
    args.update(csrf(request))
    template_name ="asignar-ejercicios.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def ejercicios_evento(request,evento_id):    
    user = request.user
    evento = get_object_or_404(Evento, id=evento_id)
    ejercicios = Ejercicios_Evento.objects.filter(evento=evento)  
    page_title = evento.nombre   
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )    
        results = Ejercicios_Evento.objects.filter(qset,evento=evento).order_by('-id')
        template_name = "ejercicios-evento.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []           
    template_name ="ejercicios-evento.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 