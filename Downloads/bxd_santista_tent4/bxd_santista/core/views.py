from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ComercioForm, ClienteForm, LoginClienteForm, LoginComercioForm
from .models import Cliente, Comercio
from django.conf import settings
from .utils import gerar_chave_acesso


def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_cliente')  # ou outro destino após cadastro
    else:
        form = ClienteForm()
    
    return render(request, 'cadastro_cliente.html', {'form': form})

def cadastro_comercio(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        estabelecimento = request.POST['estabelecimento']
        cnpj = request.POST['cnpj']

        chave = gerar_chave_acesso()

        comercio = Comercio.objects.create(
            nome=nome,
            email=email,
            estabelecimento=estabelecimento,
            cnpj=cnpj,
            chave_acesso=chave
        )

        send_mail(
            'Chave de Acesso - BXD Santista',
            f'Sua chave de acesso é: {chave}\nUse essa chave junto com seu CNPJ para fazer login.',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        return redirect('login_comercio')

    form = ComercioForm()
    return render(request, 'cadastro_comercio.html', {'form': form})

def login_cliente(request):
    if request.method == 'POST':
        form = LoginClienteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            senha = form.cleaned_data['senha']
            
            cliente = Cliente.objects.filter(nome=nome).first()
            if cliente:
                if cliente.senha == senha:
                    request.session['cliente_id'] = cliente.id
                    messages.success(request, 'Login realizado com sucesso!')
                    return redirect('home_cliente')
                else:
                    messages.error(request, 'Senha incorreta.')
            else:
                messages.error(request, 'Nome de usuário não encontrado.')
    else:
        form = LoginClienteForm()
    
    return render(request, 'login_cliente.html', {'form': form})

def login_comercio(request):
    if request.method == 'POST':
        cnpj = request.POST['cnpj']
        chave = request.POST['chave_acesso']

        try:
            comercio = Comercio.objects.get(cnpj=cnpj, chave_acesso=chave)
            # Autenticação simples (você pode usar session para login real)
            request.session['comercio_id'] = comercio.id
            return redirect('painel_comercio')  # redirecione como preferir
        except Comercio.DoesNotExist:
            return render(request, 'login_comercio.html', {'erro': 'CNPJ ou chave incorretos.'})

    return render(request, 'login_comercio.html')

def escolha(request):
    return render(request, 'escolha.html')

def home_cliente(request):
    return render(request, 'home_cliente.html')

def home_comercio(request):
    return render(request, 'home_comercio.html')

def home(request):
    return render(request, 'home.html')