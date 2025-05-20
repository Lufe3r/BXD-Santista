from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  

class Comercio(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    estabelecimento = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    senha = models.CharField(max_length=128)

