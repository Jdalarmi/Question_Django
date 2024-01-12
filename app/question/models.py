from django.db import models

class Pergunta(models.Model):
    texto = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.texto
    
class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.texto

class RespostaUsuario(models.Model):
    pergunta= models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta= models.ForeignKey(Resposta, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=250, default="Usuario teste")
