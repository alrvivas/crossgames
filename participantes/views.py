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
def registro_participantes(request):
    page_title = "registro de participantes"
    user = request.user
    equipos = Equipo.objects.all()
    participante = Participante.objects.all()
    if request.method == 'POST':
        form_participante = participanteForm(request.POST,request.FILES)
        if form_participante.is_valid():
            participante = form_participante.save(commit = False)
            participante.save()            
            return redirect(participante.get_absolute_url())
    else:
        form_participante = participanteForm()
    args = {}
    args.update(csrf(request))
    template_name ="registro-participantes.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def participantes(request):
    page_title = "Participantes"
    user = request.user
    participantes = Participante.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )    
        results = Participante.objects.filter(qset).order_by('-id')
        template_name = "resultados-participantes.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="participantes.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def participante(request,participante_id):
    user = request.user
    participante = get_object_or_404(Participante, id=participante_id)
    page_title = participante.nombre_completo     
    template_name ="participante.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))