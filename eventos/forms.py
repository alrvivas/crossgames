#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.core.files.images import get_image_dimensions
from PIL import Image
from .models import Evento,Ejercicios_Evento

class eventoForm(ModelForm):
	class Meta:
		model = Evento
		fields = '__all__'

class addejericiciosForm(ModelForm):
	class Meta:
		model = Ejercicios_Evento
		fields = '__all__'