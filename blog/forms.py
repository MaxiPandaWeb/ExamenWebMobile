from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Orden

class OrdenForm(forms.ModelForm):
	class Meta:
		model = Orden
		fields = ['cliente_or', 'fecha_or', 'hora_inicio' , 'hora_termino','id_ascensor','modelo_ascensor',
				  'fallos_detectados', 'reparaciones_or','piezas_or','estado_or','nom_user']

