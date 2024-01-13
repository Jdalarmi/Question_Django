from django.contrib import admin
from .models import Pergunta, Resposta, RespostaUsuario

class RespostaInline(admin.TabularInline):
    """Utilização da classe TabularInline para melhor ajuste das perguntas e respostas no Admin
    simulando uma tabela com coluna e linhas"""
    model = Resposta
    extra = 1

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInline]

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(RespostaUsuario)
