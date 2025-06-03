from django.urls import path
from . import views  # ou outro app que tenha a view

urlpatterns = [
    path('', views.home, name='home'),
    path('escolha',views.escolha, name='escolha'),
    path('cadastro/cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('cadastro/comercio/', views.cadastro_comercio, name='cadastro_comercio'),
    path('login/cliente',views.login_cliente, name='login_cliente'),
    path('login/comercio',views.login_comercio, name='login_comercio'),
    path('home/cliente',views.home_cliente, name='home_cliente'),
    path('home/comercio',views.home_comercio, name='home_comercio'),
    
    
]

#path('',views., name=''),