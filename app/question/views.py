from django.shortcuts import render, redirect
from .forms import RespostaUsuarioForm
from .models import Pergunta
from django.contrib import messages

def question_user_test(request):
    questions = Pergunta.objects.all()

    if request.method == 'POST':
        """Verifica se requisição foi POST para processar o formulario enviado"""
        forms = [RespostaUsuarioForm(id_da_pergunta=question.id, data=request.POST, prefix=str(question.id)) for question in questions]
        if all(form.is_valid() for form in forms):
            """Consulta os formularios verificando a validade de ambos no for loop"""
            for form in forms:
                form.save()
            return redirect('confirmation')
        else:
            messages.error(request, 'Por favor todos campos precisam ser preenchidos!')
            return redirect('home-page')
    else:
        """Inicializa formulario passando argumento id da pergunta para o form 
        o prefix permite que se houver mais de uma pergunta exemplo ID 1 e 2 elas terão o prefixo diferente
        facilitando lidar com formulario na volta da requisição."""
        forms = [RespostaUsuarioForm(id_da_pergunta=question.id, prefix=str(question.id)) for question in questions]

    context = {'forms': forms}
    return render(request, 'question/questions.html', context)


def confimation_request(request):
    return render(request, 'question/confimation.html')