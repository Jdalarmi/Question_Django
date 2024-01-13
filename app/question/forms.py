from django import forms
from .models import RespostaUsuario, Pergunta, Resposta

class RespostaUsuarioForm(forms.ModelForm):
    class Meta:
        model = RespostaUsuario
        fields = ['pergunta', 'resposta']

    def __init__(self, id_da_pergunta, *args, **kwargs):
        """Metodo construtor que recebe id da pergunta para assim referenciar as respostas pertencentes
        ao ID fornecido"""
        super(RespostaUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['pergunta'].queryset = Pergunta.objects.filter(id=id_da_pergunta)
        self.fields['resposta'].queryset = Resposta.objects.filter(pergunta_id=id_da_pergunta)

        