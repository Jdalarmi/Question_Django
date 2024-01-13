from django.test import TestCase
from question.forms import RespostaUsuarioForm
from question.models import Pergunta, Resposta

class TestFormEmpty(TestCase):
    """Simulando a criação de pergunta e reposta para ser usado no teste"""
    def setUp(self):
        self.pergunta = Pergunta.objects.create(texto='Qual é a sua cor favorita?')
        self.resposta = Resposta.objects.create(pergunta=self.pergunta, texto='Azul')

    def test_form_does_not_cotain_data(self):
        """Teste para verificar se formulario contem os dados e é valido"""
        data = {'pergunta': self.pergunta.id, 'resposta': self.resposta.id}
        form = RespostaUsuarioForm(id_da_pergunta=self.pergunta.id, data=data)
        self.assertTrue(form.is_valid())
