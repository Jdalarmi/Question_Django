from django.shortcuts import render
from .forms import RespostaUsuarioForm
from .models import Pergunta

def home_page(request):
    """Renderizando a pagina inicial de perguntas e respostas"""

    form = RespostaUsuarioForm()
    context = {'form':form}
    
    return render(request, 'question/questions.html', context)
