from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .models import Empleado
from competencias.models import Competencia
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q  

def LoginView(request):
    if not request.user.is_anonymous():
        return redirect('index')
    if request.POST:
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return redirect('index')
                else:
                    return render_to_response('inactivousuario.html', context_instance=RequestContext(request))#no activo
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))#no usuario
    else:
        formulario = AuthenticationForm()
    page_title = "Ingreso de Usuarios"
    return render_to_response('login.html',{'formulario':formulario,'page_title':page_title}, context_instance=RequestContext(request))

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')

def index(request):
    page_title = "Competencias"
    user = request.user
    competencias = Competencia.objects.all()
    template ="index.html" 
    return render_to_response(template, locals(),context_instance=RequestContext(request))