from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return HttpResponse

def index(request):
    return render(request, 'index.html')

def Escolha(request):
    return render(request, 'Escolha.html')

def cadastro_cliente(request):
    return render(request, 'cadastro_cliente.html')

def cadastro_comercio(request):
    return render(request, 'cadastro_comércio.html')

def login_cliente(request):
    return render(request, 'login_cliente.html')

def login_comercio(request):
    return render(request, 'login_comércio.html')

def home_cliente(request):
    return render(request, "home_cliente.html")