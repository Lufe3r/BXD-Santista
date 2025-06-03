import random
import string

def gerar_chave_acesso(tamanho=12):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=tamanho))