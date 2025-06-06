from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ComercioForm, ClienteForm, LoginClienteForm, LoginComercioForm, ProdutoForm, ComercioPerfilForm, ClientePerfilForm
from .models import Cliente, Comercio, Produto, TIPOS_COMERCIO
from django.conf import settings
from django.db.models import Max


def home(request):
    return render(request, 'home.html')

def escolha(request):
    return render(request, 'escolha.html')

def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)  
            senha = form.cleaned_data['senha']
            cliente.set_senha(senha)          
            cliente.save()                     
            return redirect('home_cliente')
    else:
        form = ClienteForm()

    return render(request, 'cadastro_cliente.html', {'form': form})

def login_cliente(request):
    if request.method == 'POST':
        form = LoginClienteForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']

            try:
                cliente = Cliente.objects.get(nome=usuario)  
                if cliente.check_senha(senha):
                    request.session['cliente_id'] = cliente.id
                    return redirect('home_cliente')
                else:
                    messages.error(request, 'Usuário ou senha inválidos.')
            except Cliente.DoesNotExist:
                messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginClienteForm()

    return render(request, 'login_cliente.html', {'form': form})


def home_cliente(request):
    return render(request, 'home_cliente.html')

def perfil_cliente(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('login_cliente')

    cliente_obj = Cliente.objects.get(id=cliente_id)

    if request.method == 'POST':
        form = ClientePerfilForm(request.POST, request.FILES, instance=cliente_obj)
        if form.is_valid():
            form.save()
            return redirect('perfil_cliente')
    else:
        form = ClientePerfilForm(instance=cliente_obj)

    return render(request, 'perfil_cliente.html', {'form': form})

def estabelecimento_favoritados(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('login_cliente')

    cliente = Cliente.objects.get(id=cliente_id)
    favoritos = cliente.favoritos.all()

    return render(request, 'estabelecimento_favoritados.html', {'favoritos': favoritos})

def comentario_cliente(request):
    return render(request, 'comentario_cliente.html')

def buscar_comercios(request):
    tipo_selecionado = request.GET.get('tipo')  # Pega o tipo selecionado na URL
    if tipo_selecionado:
        comercios = Comercio.objects.filter(tipo_comercio=tipo_selecionado)
    else:
        comercios = Comercio.objects.all()

    return render(request, 'buscar_comercios.html', {
        'comercios': comercios,
        'tipos': TIPOS_COMERCIO,
        'tipo_selecionado': tipo_selecionado,
    })

def perfil_comercio_publico(request, comercio_id):
    comercio = get_object_or_404(Comercio, id=comercio_id)
    cliente_id = request.session.get('cliente_id')
    cliente = Cliente.objects.get(id=cliente_id) if cliente_id else None

    return render(request, 'perfil_comercio_publico.html', {
        'comercio': comercio,
        'cliente': cliente,
    })

def ver_catalogo(request, comercio_id):
    comercio = Comercio.objects.get(id=comercio_id)
    produtos = Produto.objects.filter(comercio=comercio)

    return render(request, 'catalogo_publico.html', {
        'comercio': comercio,
        'produtos': produtos
    })

def favoritar_comercio(request, comercio_id):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('login_cliente')  # ou redirecione conforme sua lógica de autenticação

    cliente = get_object_or_404(Cliente, id=cliente_id)
    comercio = get_object_or_404(Comercio, id=comercio_id)

    if comercio in cliente.favoritos.all():
        cliente.favoritos.remove(comercio)
    else:
        cliente.favoritos.add(comercio)

    return redirect('perfil_comercio_publico', comercio_id=comercio.id)

#PARTE DO COMERCIO

def cadastro_comercio(request):
    if request.method == 'POST':
        form = ComercioForm(request.POST)
        if form.is_valid():
            comercio = form.save(commit=False) 
            senha = form.cleaned_data['senha']
            comercio.set_senha(senha)          
            comercio.save()                     
            return redirect('login_comercio')
    else:
        form = ComercioForm()
    return render(request, 'cadastro_comercio.html', {'form': form})

def login_comercio(request):
    if request.method == 'POST':
        form = LoginComercioForm(request.POST)
        if form.is_valid():
            cnpj = form.cleaned_data['cnpj']
            senha = form.cleaned_data['senha']

            try:
                comercio = Comercio.objects.get(cnpj=cnpj)
                if comercio.check_senha(senha):
                    request.session['comercio_id'] = comercio.id
                    return redirect('home_comercio')
                else:
                    messages.error(request, 'Senha incorreta.')
            except Comercio.DoesNotExist:
                messages.error(request, 'CNPJ não encontrado.')
        else:
            messages.error(request, 'Formulário inválido.')
    else:
        form = LoginComercioForm()

    return render(request, 'login_comercio.html', {'form': form})

def home_comercio(request):
    comercio_id = request.session.get('comercio_id')
    if not comercio_id:
        return redirect('login_comercio')

    produto_mais_vendido = Produto.objects.filter(comercio_id=comercio_id).order_by('-vendidos').first()
    produtos_em_falta = Produto.objects.filter(comercio_id=comercio_id, estoque=0)

    context = {
        'produto_mais_vendido': produto_mais_vendido,
        'produtos_em_falta': produtos_em_falta,
    }

    return render(request, 'home_comercio.html', context)

def perfil_comercio(request):
    comercio_id = request.session.get('comercio_id')
    comercio_obj = Comercio.objects.get(id=comercio_id)

    if request.method == 'POST':
        form = ComercioPerfilForm(request.POST, request.FILES, instance=comercio_obj)  # <- Aqui também
        if form.is_valid():
            form.save()
            return redirect('perfil_comercio')
    else:
        form = ComercioPerfilForm(instance=comercio_obj)

    return render(request, 'perfil_comercio.html', {'form': form})


def estoque(request):
    comercio_id = request.session.get('comercio_id')
    if not comercio_id:
        return redirect('login_comercio')

    produtos = Produto.objects.filter(comercio_id=comercio_id).order_by('numero_local')
    return render(request, 'estoque.html', {'produtos': produtos})


def adicionar_produto(request):
    comercio_id = request.session.get('comercio_id')
    if not comercio_id:
        return redirect('login_comercio')

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.comercio_id = comercio_id

            # Pega o maior numero_local atual daquele comércio
            ultimo_numero = Produto.objects.filter(comercio_id=comercio_id).aggregate(
                Max('numero_local')
            )['numero_local__max'] or 0

            produto.numero_local = ultimo_numero + 1
            produto.save()

            return redirect('estoque')
    else:
        form = ProdutoForm()
    return render(request, 'form_produto.html', {'form': form})

def editar_produto(request, produto_id):
    comercio_id = request.session.get('comercio_id')
    if not comercio_id:
        return redirect('login_comercio')

    produto = get_object_or_404(Produto, id=produto_id, comercio_id=comercio_id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)  # <- Adicione isso aqui
        if form.is_valid():
            produto = form.save(commit=False)
            produto.comercio_id = comercio_id 
            produto.save()
            return redirect('estoque')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'form_produto.html', {'form': form, 'produto': produto})

def remover_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('estoque')
    return render(request, 'confirmar_remocao.html', {'produto': produto})

def comercio_codigo_compra(request):
    return render(request, 'comercio_codigo_compra.html')


def feedback_produtos(request):
    return render(request, 'feedback_produtos.html')
