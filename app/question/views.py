# views.py
from django.shortcuts import render, redirect
from .forms import RespostaUsuarioForm
from .models import Pergunta

def home_page(request):

    perguntas = Pergunta.objects.all()

    if request.method == 'POST':
        forms = [RespostaUsuarioForm(request.POST, prefix=f'form_{pergunta.id}') for pergunta in perguntas]
        if all(form.is_valid() for form in forms):
            for form in forms:
                form.save()
            return redirect('home-page')
    else:
        forms = [RespostaUsuarioForm(prefix=f'form_{pergunta.id}') for pergunta in perguntas]

    context = {'forms':forms}
    return render(request, 'question/questions.html', context)
