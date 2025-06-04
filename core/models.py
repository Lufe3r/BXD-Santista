from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Cliente(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def set_senha(self, raw_password):
        self.senha = make_password(raw_password)

    def check_senha(self, raw_password):
        return check_password(raw_password, self.senha)

    def __str__(self):
        return self.nome

class Comercio(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    estabelecimento = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    senha = models.CharField(max_length=100)

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
    estoque = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    catalogo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome