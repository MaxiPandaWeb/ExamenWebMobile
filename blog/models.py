from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	nom_cli = models.CharField(max_length=100)
	direc_cli = models.CharField(max_length=100)
	ciudad_cli = models.CharField(max_length=100)
	comuna_cli = models.CharField(max_length=100)
	telefono_cli = models.CharField(max_length=100)
	correo_cli = models.EmailField(max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)
	tecnico = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.nom_cli

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

class Orden(models.Model):
	folio_or = models.AutoField(primary_key=True)
	cliente_or = models.ForeignKey(Post, on_delete=models.CASCADE)
	fecha_or = models.DateTimeField(default=timezone.now)
	hora_inicio = models.DateTimeField(default=timezone.now)
	hora_termino = models.DateTimeField(default=timezone.now)
	id_ascensor = models.IntegerField()
	modelo_ascensor = models.CharField(max_length=100)
	fallos_detectados = models.TextField(max_length=100)
	reparaciones_or = models.TextField(max_length=100)
	piezas_or = models.TextField(max_length=100)
	estado_or = models.CharField(max_length=100)
	nom_user = models.ForeignKey(User, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('orden', kwargs={'pk': self.pk})