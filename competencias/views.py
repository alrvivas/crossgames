# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg,Sum
from .models import *
from eventos.models import *
from .forms import *
from django.contrib.auth.models import User
from django.db.models import Q 
from django.forms.models import modelformset_factory

@login_required(login_url='/login/')
def registro_competencias(request):
    page_title = "registro de competencia"
    user = request.user
    competencia = Competencia.objects.all()
    if request.method == 'POST':
        form_competencia = competenciaForm(request.POST,request.FILES)
        if form_competencia.is_valid():
            competencia = form_competencia.save(commit = False)
            competencia.save()            
            return redirect(competencia.registro_ejercicios_evento())
    else:
        form_competencia = competenciaForm()
    args = {}
    args.update(csrf(request))
    template_name ="registro-competencia.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def competencias(request):
    page_title = "Competencias"
    user = request.user
    competencia = Competencia.objects.all()   
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )    
        results = Competencia.objects.filter(qset).order_by('-id')
        template_name = "resultados-competencias.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="competencias.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

def competencia(request,competencia_id):
    user = request.user
    competencia = get_object_or_404(Competencia, id=competencia_id)
    eventos = Evento.objects.filter(competencia=competencia)
    page_title = competencia.nombre
    template_name ="competencia.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 
