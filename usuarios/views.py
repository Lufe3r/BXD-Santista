from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import Cliente, Comercio  # modelo do vendedor

def cadastro_cliente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        confirma = request.POST['confirma_senha']
    if check_password(senha, Cliente.senha):
        return redirect('pagina_cliente')
    return render(request, 'cadastro_cliente.html')

def cadastro_comercio(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        estabelecimento = request.POST['estabelecimento']
        cnpj = request.POST['cnpj']
        senha = request.POST['senha']

        if check_password(senha, Comercio.usuario.password):
            return redirect('pagina_comercio')
    return render(request, 'cadastro_comercio.html')


def login_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            cliente = Cliente.objects.get(email=email)
            if cliente.senha == senha:
                return redirect('pagina_cliente')
            else:
                messages.error(request, "Senha incorreta.")
        except Cliente.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")
    
    return render(request, 'login_cliente.html')


def login_comercio(request):
    if request.method == 'POST':
        cnpj = request.POST.get('cnpj')
        senha = request.POST.get('senha')

        try:
            comercio = Comercio.objects.get(cnpj=cnpj)
            if comercio.senha == senha:
                # Sucesso no login
                return redirect('pagina_comercio')
            else:
                messages.error(request, "Senha incorreta.")
        except Comercio.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")
    
    return render(request, 'login_comercio.html')
