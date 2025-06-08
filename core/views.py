from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ComercioForm, ClienteForm, LoginClienteForm, LoginComercioForm, ProdutoForm, ComercioPerfilForm, ClientePerfilForm
from .models import Cliente, Comercio, Produto, TIPOS_COMERCIO, CompraFinalizada
from django.conf import settings
from django.db.models import Max
from django.http import HttpResponse
import random, re, string

def cliente_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_cliente')
        if not hasattr(request.user, 'cliente'):
            messages.error(request, 'Apenas clientes podem acessar essa página.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def comercio_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_comercio')
        if not hasattr(request.user, 'comercio'):
            messages.error(request, 'Apenas comércios podem acessar essa página.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


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

            # Cria usuário Django
            user = User.objects.create_user(username=cliente.nome, email=cliente.email, password=senha)

            cliente.user = user  # Associa cliente ao User criado
            cliente.set_senha(senha)
            cliente.save()

            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login_cliente')
    else:
        form = ClienteForm()

    return render(request, 'cadastro_cliente.html', {'form': form})

def login_cliente(request):
    if request.method == 'POST':
        form = LoginClienteForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']

            user = authenticate(request, username=usuario, password=senha)
            if user is not None:
                login(request, user)
                return redirect('home_cliente')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginClienteForm()

    return render(request, 'login_cliente.html', {'form': form})


def home_cliente(request):
    return render(request, 'home_cliente.html')

@cliente_required
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

@cliente_required
def estabelecimento_favoritados(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('login_cliente')

    cliente = Cliente.objects.get(id=cliente_id)
    favoritos = cliente.favoritos.all()

    return render(request, 'estabelecimento_favoritados.html', {'favoritos': favoritos})

@cliente_required
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
    produtos = Produto.objects.filter(comercio_id=comercio_id)

    return render(request, 'perfil_comercio_publico.html', {
        'comercio': comercio,
        'produtos': produtos
    })

def ver_catalogo(request, comercio_id):
    comercio = Comercio.objects.get(id=comercio_id)
    produtos = Produto.objects.filter(comercio=comercio)

    return render(request, 'ver_catalogo.html', {
        'comercio': comercio,
        'produtos': produtos
    })


def favoritar_comercio(request, comercio_id):
    print("Usuário logado:", request.user)
    print("É cliente?", hasattr(request.user, 'cliente'))
    cliente = get_object_or_404(Cliente, user=request.user)
    comercio = get_object_or_404(Comercio, id=comercio_id)

    if comercio in cliente.favoritos.all():
        cliente.favoritos.remove(comercio)
    else:
        cliente.favoritos.add(comercio)

    return redirect('perfil_comercio_publico', comercio_id=comercio.id)

@cliente_required
def carrinho(request):
    carrinho = request.session.get('carrinho', {})
    
    if not isinstance(carrinho, dict):
        carrinho = {}
        request.session['carrinho'] = carrinho 

    produtos = []
    total = 0

    for produto_id, quantidade in carrinho.items():
        produto = Produto.objects.get(id=produto_id)
        subtotal = produto.preco * quantidade
        total += subtotal
        produtos.append({
            'produto': produto,
            'quantidade': quantidade,
            'subtotal': subtotal
        })

    return render(request, 'carrinho.html', {'produtos': produtos, 'total': total})

def adicionar_ao_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    carrinho[str(produto_id)] = carrinho.get(str(produto_id), 0) + 1
    request.session['carrinho'] = carrinho
    return redirect('ver_catalogo', comercio_id=Produto.objects.get(id=produto_id).comercio_id)

@cliente_required
def finalizar_compra(request):
    if request.method == 'POST':
        pagamento = request.POST.get('pagamento')
        carrinho = request.session.get('carrinho', {})

        if not carrinho:
            return HttpResponse("Carrinho vazio.")

        produtos_lista = []
        total = 0

        for produto_id, quantidade in carrinho.items():
            produto = Produto.objects.get(id=produto_id)

            if produto.estoque < quantidade:
                return HttpResponse(f"Estoque insuficiente para o produto: {produto.nome}")

            subtotal = produto.preco * quantidade
            total += subtotal

            # Subtrai do estoque
            produto.estoque -= quantidade
            produto.save()

            produtos_lista.append({
                'produto_id': produto.id,
                'nome': produto.nome,
                'quantidade': quantidade,
                'subtotal': float(subtotal),
            })

        codigo = gerar_codigo()

        compra = CompraFinalizada.objects.create(
            codigo=codigo,
            usuario=request.user,
            comercio=Produto.objects.get(id=list(carrinho.keys())[0]).comercio,
            produtos=produtos_lista,
            total=total
        )

        request.session['carrinho'] = {}  # limpa o carrinho

        return HttpResponse(f'Compra finalizada com sucesso! Código para retirada: {codigo}')

    return redirect('carrinho')

@cliente_required
def cancelar_pedido(request):
    request.session['carrinho'] = {}  # ← dicionário, não lista
    return redirect('carrinho')

def gerar_codigo(tamanho=5):
    caracteres = string.ascii_uppercase + string.digits
    while True:
        codigo = ''.join(random.choice(caracteres) for _ in range(tamanho))
        if not CompraFinalizada.objects.filter(codigo=codigo).exists():
            return codigo

#PARTE DO COMERCIO

def limpa_cnpj(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def cadastro_comercio(request):
    if request.method == 'POST':
        form = ComercioForm(request.POST)
        if form.is_valid():
            print("Formulário válido.")
            comercio = form.save(commit=False)
            senha = form.cleaned_data['senha']
            print("Senha digitada:", senha)

            cnpj_limpo = limpa_cnpj(comercio.cnpj)
            print("CNPJ limpo:", cnpj_limpo)

            if User.objects.filter(username=cnpj_limpo).exists():
                print("CNPJ já existe no banco.")
                messages.error(request, 'CNPJ já cadastrado.')
            else:
                comercio.cnpj = cnpj_limpo
                user = User.objects.create_user(username=cnpj_limpo, password=senha)
                comercio.user = user
                comercio.set_senha(senha)
                comercio.save()
                print("Usuário e comércio criados com sucesso.")
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('login_comercio')
        else:
            print("Erros no formulário:", form.errors)
            messages.error(request, 'Formulário inválido. Verifique os dados.')
    else:
        form = ComercioForm()

    return render(request, 'cadastro_comercio.html', {'form': form})


def login_comercio(request):
    if request.method == 'POST':
        form = LoginComercioForm(request.POST)
        if form.is_valid():
            cnpj = limpa_cnpj(form.cleaned_data['cnpj'])
            senha = form.cleaned_data.get('senha')

            user = authenticate(request, username=cnpj, password=senha)
            if user is not None:
                login(request, user)
                try:
                    comercio = Comercio.objects.get(user=user)
                    request.session['comercio_id'] = comercio.id
                except Comercio.DoesNotExist:
                    messages.error(request, 'Comércio não encontrado.')
                    return redirect('login_comercio')

                return redirect('home_comercio')
            else:
                messages.error(request, 'CNPJ ou senha inválidos.')
    else:
        form = LoginComercioForm()

    return render(request, 'login_comercio.html', {'form': form})


@comercio_required
def home_comercio(request):
    comercio = request.user.comercio
    produto_mais_vendido = Produto.objects.filter(comercio=comercio).order_by('-vendidos').first()
    produtos_em_falta = Produto.objects.filter(comercio=comercio, estoque=0)
    compra = CompraFinalizada.objects.filter(comercio=comercio, entregue=False).first()

    context = {
        'produto_mais_vendido': produto_mais_vendido,
        'produtos_em_falta': produtos_em_falta,
        'compra': compra,
    }

    return render(request, 'home_comercio.html', context)


@comercio_required
def perfil_comercio(request):
    comercio = request.user.comercio

    if request.method == 'POST':
        form = ComercioPerfilForm(request.POST, request.FILES, instance=comercio)
        if form.is_valid():
            form.save()
            return redirect('perfil_comercio')
    else:
        form = ComercioPerfilForm(instance=comercio)

    return render(request, 'perfil_comercio.html', {'form': form})


@comercio_required
def estoque(request):
    comercio = request.user.comercio
    produtos = Produto.objects.filter(comercio=comercio).order_by('numero_local')
    return render(request, 'estoque.html', {'produtos': produtos})


@comercio_required
def adicionar_produto(request):
    comercio = request.user.comercio
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.comercio = comercio

            ultimo_numero = Produto.objects.filter(comercio=comercio).aggregate(
                Max('numero_local')
            )['numero_local__max'] or 0

            produto.numero_local = ultimo_numero + 1
            produto.save()

            return redirect('estoque')
    else:
        form = ProdutoForm()
    return render(request, 'form_produto.html', {'form': form})


@comercio_required
def editar_produto(request, produto_id):
    comercio = request.user.comercio
    produto = get_object_or_404(Produto, id=produto_id, comercio=comercio)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('estoque')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'form_produto.html', {'form': form, 'produto': produto})


@comercio_required
def remover_produto(request, produto_id):
    comercio = request.user.comercio
    produto = get_object_or_404(Produto, id=produto_id, comercio=comercio)
    if request.method == 'POST':
        produto.delete()
        return redirect('estoque')
    return render(request, 'confirmar_remocao.html', {'produto': produto})


@comercio_required
def comercio_codigo_compra(request, codigo):
    compra = get_object_or_404(CompraFinalizada, codigo=codigo)
    return render(request, 'comercio_codigo_compra.html', {'compra': compra})


@comercio_required
def marcar_entregue(request, codigo):
    compra = get_object_or_404(CompraFinalizada, codigo=codigo)
    compra.entregue = True
    compra.save()
    return redirect('comercio_codigo_compra', codigo=codigo)


@comercio_required
def feedback_produtos(request):
    return render(request, 'feedback_produtos.html')
