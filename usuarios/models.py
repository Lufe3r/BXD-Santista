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
    
class Cormercio_produtos(models.Model):
    Imagem = models.ImageField(upload_to='')
    nome_produto = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    estoque = models.CharField(500)
    preco = models.CharField(10)
    descricao = models.CharField(200)
    catalogo = models.CharField(50)

class Cliente_perfil(models.Model):
    imagem_perfil = models.ImageField(upload_to='')
    comentarios = models.CharField(max_length=200)
    historico = models.CharField(max_length= 100)


