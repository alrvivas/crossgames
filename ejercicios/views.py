# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg,Sum
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.db.models import Q 

@login_required(login_url='/login/')
def registro_ejercicios(request):
    page_title = "registro de ejercicios"
    user = request.user
    ejercicio = Ejercicio.objects.all()
    if request.method == 'POST':
        form_ejercicio = ejercicioForm(request.POST,request.FILES)
        if form_ejercicio.is_valid():
            ejercicio = form_ejercicio.save(commit = False)
            ejercicio.save()            
            return redirect(ejercicio.get_absolute_url())
    else:
        form_ejercicio = ejercicioForm()
    args = {}
    args.update(csrf(request))
    template_name ="registro-ejercicios.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def ejercicios(request):
    page_title = "Ejercicios"
    user = request.user
    ejercicios = Ejercicio.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )    
        results = Evento.objects.filter(qset).order_by('-id')
        template_name = "resultados-ejercicios.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="ejercicios.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

def ejercicio(request,ejercicio_id):    
    user = request.user
    ejercicio = get_object_or_404(Ejercicio, id=ejercicio_id)
    page_title = ejercicio.nombre
    template_name ="ejercicio.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 