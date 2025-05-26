from django import forms
from .models import Cliente


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
