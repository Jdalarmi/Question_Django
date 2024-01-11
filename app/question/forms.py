from django import forms
from .models import Pergunta, Resposta, RespostaUsuario


class PerguntaForm(forms.ModelForm):
    """Criando formulario de pergunta para usuario"""
    class Meta:
        model = Pergunta
        fields = ('texto',)


class RespostaForm(forms.ModelForm):
    """Criando formulario de Resposta para usuario"""
    class Meta:
        model = Resposta
        fields = ('texto_resposta',)