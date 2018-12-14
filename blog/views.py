from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import OrdenForm
from django.http import HttpResponse
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Post, Orden

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request,'blog/home.html',context)

class PostListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

def list_orden(request):
	context = {
		'ordens': Orden.objects.all()
	}
	return render(request,'blog/lista_orden.html',context)

class OrdenListView(LoginRequiredMixin, ListView):
	model = Orden
	template_name = 'blog/lista_orden.html'
	context_object_name = 'ordens'
	ordering = ['-fecha_or']
	paginate_by = 5



class UserPostListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(tecnico=user).order_by('-date_posted')

class PostDetailView(LoginRequiredMixin, DetailView):
	model = Post
	

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['nom_cli','direc_cli','ciudad_cli','comuna_cli','telefono_cli','correo_cli','tecnico']



class OrdenCreateView(LoginRequiredMixin,CreateView):
	model = Orden
	fields = ['cliente_or', 'fecha_or', 'hora_inicio' , 'hora_termino','id_ascensor','modelo_ascensor',
			  'fallos_detectados', 'reparaciones_or','piezas_or','estado_or','nom_user']
	success_url = '/'
	def form_valid(self, form):
		form.instance.tecnico = self.request.user
		return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['nom_cli','direc_cli','ciudad_cli','comuna_cli','telefono_cli','correo_cli','tecnico']

	def form_valid(self, form):
		form.instance.tecnico = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.tecnico:
			return True
		return False

class OrdenUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Orden
	success_url = '/'
	fields = ['cliente_or', 'fecha_or', 'hora_inicio' , 'hora_termino','id_ascensor','modelo_ascensor',
			  'fallos_detectados', 'reparaciones_or','piezas_or','estado_or','nom_user']

	def form_valid(self, form):
		form.instance.nom_user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		orden = self.get_object()
		if self.request.user == orden.nom_user:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.tecnico:
			return True
		return False	
			

@login_required
def orden_crear(request):
	if request.method == 'POST':
		u_form = OrdenForm(request.POST, instance=request.user)
		if u_form.is_valid():
			#cliente_or = Post.objects.get("nom_cli")
			u_form.save()
			return redirect('orden-crear')
	else:
		u_form = OrdenForm(instance=request.user)
	context = {
		'u_form': u_form,

	}
	return render(request, 'blog/orden.html',context)