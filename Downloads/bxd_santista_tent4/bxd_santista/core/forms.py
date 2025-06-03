from django import forms
from .models import Cliente, Comercio

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
    class Meta:
        model = Comercio
        fields = ['nome', 'email', 'estabelecimento', 'cnpj']
  
class LoginClienteForm(forms.Form):
    nome = forms.CharField(label='Nome')
    senha = forms.CharField(widget=forms.PasswordInput)

class LoginComercioForm(forms.Form):
    cnpj = forms.CharField(max_length=18)
    chave_acesso = forms.CharField(max_length=32)