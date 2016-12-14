#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.core.files.images import get_image_dimensions
from PIL import Image
from .models import Hit,Equipos_Hit

class hitForm(ModelForm):
	class Meta:
		model = Hit
		fields = '__all__'


class addequiposForm(ModelForm):
	class Meta:
		model = Equipos_Hit
		fields = '__all__'