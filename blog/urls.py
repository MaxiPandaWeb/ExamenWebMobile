from django.urls import path
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView, 
	PostUpdateView, 
	PostDeleteView,
	UserPostListView,
	OrdenListView,
	orden_crear,
	OrdenCreateView,
	OrdenUpdateView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('orden/', OrdenListView.as_view(), name='lista-orden'),
    path('orden-crear/', OrdenCreateView.as_view(), name='orden-crear'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('orden/<int:pk>/update/', OrdenUpdateView.as_view(), name='orden-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]