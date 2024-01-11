from django import forms
from .models import RespostaUsuario, Resposta, Pergunta

class RespostaUsuarioForm(forms.ModelForm):
    class Meta:
        model = RespostaUsuario
        fields = ['resposta']
        widgets = {
            'resposta': forms.RadioSelect(), 
        }

    def __init__(self, *args, **kwargs):
        super(RespostaUsuarioForm, self).__init__(*args, **kwargs)

        pergunta_fixa_id = 5
        pergunta_fixa = Pergunta.objects.get(pk=pergunta_fixa_id)
        respostas = Resposta.objects.filter(pergunta=pergunta_fixa_id)

        self.fields['resposta'].label = pergunta_fixa.texto
        self.fields['resposta'].widget.choices = [
            (resposta.id, resposta.texto) for resposta in respostas
        ]

        self.fields['resposta'].empty_label = None

