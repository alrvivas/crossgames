#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.core.files.images import get_image_dimensions
from PIL import Image
from .models import Competencia

class competenciaForm(ModelForm):
	class Meta:
		model = Competencia
		fields = '__all__'
