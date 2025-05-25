"""
URL configuration for bxd_santista project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.index, name='index'),
    path('escolha/', views.Escolha, name='escolha'),
    path('cadastro/cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('cadastro/comercio/', views.cadastro_comercio, name='cadastro_comercio'),
    path('login/', views.login_cliente, name='login_cliente'),
    path('login/', views.login_comercio, name='login_comercio'),
    path('home/cliente', views.home_cliente, name='home_cliente'),
]