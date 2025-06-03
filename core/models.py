from django.db import models
import uuid

class Cliente(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Comercio(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    estabelecimento = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    senha = models.CharField(max_length=128)
    chave_acesso = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.estabelecimento