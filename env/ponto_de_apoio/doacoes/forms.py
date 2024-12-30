from django import forms
from .models import Doacao
from .models import Contato

class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['nome', 'email', 'telefone', 'cidade_bairro', 'itens']

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome','email','mensagem']

class ReceberForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['nome', 'email', 'telefone', 'cidade_bairro', 'itens']