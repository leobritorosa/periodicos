from django.urls import path
from . import views

urlpatterns = [
    # O segredo está no final da linha: name='home'
    path('', views.home, name='home'),
    path('publicacao/<int:pk>/', views.detalhe_publicacao, name='detalhe_publicacao'), 
]