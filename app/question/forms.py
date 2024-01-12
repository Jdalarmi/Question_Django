
# forms.py
from django import forms
from .models import RespostaUsuario

class RespostaUsuarioForm(forms.ModelForm):
    class Meta:
        model = RespostaUsuario
        fields = ['pergunta', 'resposta']
