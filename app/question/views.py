from django.shortcuts import render
from .forms import PerguntaForm

def home_page(request):
    """Renderizando a pagina inicial de perguntas e respostas"""
    context = {}
    form = PerguntaForm
    context['form'] = form
    return render(request, 'question/questions.html', context)
