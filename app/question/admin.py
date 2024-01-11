from django.contrib import admin
from .models import Pergunta, Resposta, RespostaUsuario

class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 2

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInline]

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(RespostaUsuario)
