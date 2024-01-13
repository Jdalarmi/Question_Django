from django.shortcuts import render, redirect
from .forms import RespostaUsuarioForm
from .models import Pergunta
from django.contrib import messages

def home_page(request):
    perguntas = Pergunta.objects.all()

    if request.method == 'POST':
        forms = [RespostaUsuarioForm(id_da_pergunta=pergunta.id, data=request.POST, prefix=str(pergunta.id)) for pergunta in perguntas]
        if all(form.is_valid() for form in forms):
            for form in forms:
                form.save()
            return redirect('confirmation')
        else:
            messages.error(request, 'Por favor todos campos precisam ser preenchidos!')
            return redirect('home-page')
    else:
        forms = [RespostaUsuarioForm(id_da_pergunta=pergunta.id, prefix=str(pergunta.id)) for pergunta in perguntas]

    context = {'forms': forms}
    return render(request, 'question/questions.html', context)


def confimation_request(request):
    return render(request, 'question/confimation.html')