from django import forms
from .models import Cliente, Comercio, Produto

class ClienteForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    confirma_senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'senha']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirma = cleaned_data.get("confirma_senha")

        if senha != confirma:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

class ComercioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    confirma_senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Comercio
        fields = ['nome', 'email', 'estabelecimento', 'cnpj', 'senha']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirma = cleaned_data.get("confirma_senha")

        if senha != confirma:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data
  
class LoginComercioForm(forms.Form):
    cnpj = forms.CharField(max_length=18, label='CNPJ')
    senha = forms.CharField(widget=forms.PasswordInput, label='Senha')

class LoginClienteForm(forms.Form):
    usuario = forms.CharField(label="Usuário", max_length=100)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'estoque', 'preco', 'catalogo']