from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # O segredo está no final da linha: name='home'
    path('', views.home, name='home'),
    path('publicacao/<int:pk>/', views.detalhe_publicacao, name='detalhe_publicacao'), 
    path('professor/', views.lista_professores, name='lista_professores'),
    path('professor/novo/', views.cadastrar_professor, name='cadastrar_professor'),
    path('publicacao/nova/', views.cadastrar_publicacao, name='cadastrar_publicacao'),
    path('professor/<int:pk>/', views.perfil_professor, name='perfil_professor'),
    
    # Rotas de Login/Logout padrão do Django
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]