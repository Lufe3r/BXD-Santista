from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    favoritos = models.ManyToManyField('Comercio', related_name='clientes_favoritaram', blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    idade = models.PositiveIntegerField(null=True, blank=True)
    genero = models.CharField(max_length=20, blank=True)
    imagem_perfil = models.ImageField(upload_to='clientes/', blank=True, null=True)


    def set_senha(self, raw_password):
        self.senha = make_password(raw_password)

    def check_senha(self, raw_password):
        return check_password(raw_password, self.senha)

    def __str__(self):
        return self.nome


class CompraFinalizada(models.Model):
    codigo = models.CharField(max_length=5, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comercio = models.ForeignKey('Comercio', on_delete=models.CASCADE)
    produtos = models.JSONField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    entregue = models.BooleanField(default=False)

    def __str__(self):
        return f'Compra {self.codigo} - {self.usuario}'

TIPOS_COMERCIO = [
    ('Mecanico', 'Mecânico'),
    ('Chaveiro', 'Chaveiro'),
    ('Acougue', 'Açougue'),
    ('Brecho', 'Brechó'),
    ('Marcenaria', 'Marcenaria'),
    ('Bijuteria', 'Bijuteria'),
    ('Pedicure', 'Pedicure'),
    ('Manicure', 'Manicure'),
    ('Cabeleireiro', 'Cabeleireiro'),
    ('Dentista', 'Dentista'),
    ('Restaurante', 'Restaurante'),
    ('Mercado', 'Mercado'),
    ('Papelaria', 'Papelaria'),
    ('Farmacia', 'Farmácia'),
    ('Livraria', 'Livraria'),
    ('Barbeiro', 'Barbeiro'),
    ('Outros', 'Outros'),
]

class Comercio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # ADICIONE ISSO

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    estabelecimento = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    senha = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    descricao = models.TextField(blank=True)
    tipo_comercio = models.CharField(
        max_length=50,
        choices=TIPOS_COMERCIO,
        default='Outros'
    )
    horario_funcionamento = models.CharField(max_length=100, blank=True)
    formas_pagamento = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255, blank=True)

    def set_senha(self, raw_password):
        self.senha = make_password(raw_password)

    def check_senha(self, raw_password):
        return check_password(raw_password, self.senha)

    def __str__(self):
        return self.estabelecimento
    
class Produto(models.Model):
    comercio = models.ForeignKey('Comercio', on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    catalogo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    numero_local = models.PositiveIntegerField(default=0)
    estoque = models.PositiveIntegerField(default=0)
    vendidos = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome


class Comentario(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    comercio = models.ForeignKey('Comercio', on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.cliente} em {self.comercio}'