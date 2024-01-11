from django.db import models

class Pergunta(models.Model):
    texto = models.CharField(max_length=250, null=False)

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_resposta = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.texto_resposta

class RespostaUsuario(models.Model):
    pergunta_user = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta_user = models.ForeignKey(Resposta, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=250)
