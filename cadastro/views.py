from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Aluno
from .forms import AlunoForm

# Create your views here.

# PAGINA PRINCIPAL
def pagina_principal(request) :
    return render(request, 'cadastro/pagina_principal.html')

# CADASTRO DE ALUNOS
def cadastrar_aluno(request) :
    if request.method == 'POST' :
        form = AlunoForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, 'Aluno cadastrado com sucesso!')
            return redirect('lista_alunos')
    else :
        form = AlunoForm()
    return render(request, 'cadastro/cadastrar_aluno.html', {'form': form})

# LISTAGEM DOS ALUNOS
def lista_alunos(request) :
    alunos = Aluno.objects.all()
    return render(request, 'cadastro/lista_alunos.html', {'alunos': alunos})

# DELETE DE ALUNOS
def excluir_aluno(request, aluno_id) :
    aluno = Aluno.objects.get(id = aluno_id)
    aluno.delete()
    messages.success(request, f'O aluno {aluno.nome} foi excluido com sucesso!')
    return redirect('lista_alunos')

# DETALHES DOS ALUNO
def detalhes_aluno(request, aluno_id) :
    aluno = get_object_or_404(Aluno, id = aluno_id)
    return render(request, 'cadastro/detalhes_aluno.html', {'aluno': aluno})

# ATUALIZAR ALUNO
def atualizar_aluno(request, aluno_id) :
    aluno = get_object_or_404(Aluno, id = aluno_id)

    if request.method == 'POST' :
        form = AlunoForm(request.POST, instance = aluno)
        if form.is_valid() :
            form.save()
            messages.success(request, f'Dados do aluno {aluno.nome} atualizados com sucesso!')
            return redirect('lista_alunos')
    else :
        form = AlunoForm(instance = aluno)
    return render(request, 'cadastro/atualizar_aluno.html', {'form': form, 'aluno': aluno})