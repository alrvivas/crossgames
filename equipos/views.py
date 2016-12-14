# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg,Sum
from .models import *
from participantes.models import *
from .forms import *
from django.contrib.auth.models import User
from django.db.models import Q 

@login_required(login_url='/login/')
def registro_equipo(request):
    page_title = "registro de equipos"
    user = request.user
    equipo = Equipo.objects.all()
    if request.method == 'POST':
        form_equipo = equipoForm(request.POST,request.FILES)
        if form_equipo.is_valid():
            equipo = form_equipo.save(commit = False)
            equipo.save()            
            return redirect(equipo.get_absolute_url())
    else:
        form_equipo = equipoForm()
    args = {}
    args.update(csrf(request))
    template_name ="registro-equipos.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def equipos(request):
    page_title = "Equipos"
    user = request.user
    equipos = Equipo.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )    
        results = Equipo.objects.filter(qset).order_by('-id')
        template_name = "resultados-equipos.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="equipos.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def equipo(request,equipo_id):
    user = request.user
    equipo = get_object_or_404(Equipo, id=equipo_id)
    page_title = equipo.nombre     
    template_name ="equipo.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

@login_required(login_url='/login/')
def equipo_participantes(request,equipo_id):
    page_title = "Participantes"
    user = request.user
    equipo = get_object_or_404(Equipo, id=equipo_id)
    participantes = Participante.objects.filter(equipo=equipo)
    template_name ="equipo-participantes.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 