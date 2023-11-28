from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Aluno, Curso
from .forms import AlunoForm, CursoForm

# Create your views here.

# PAGINA PRINCIPAL
def pagina_principal(request) :
    contexto = {
        'url_cadastrar_curso': 'cadastrar_curso',
        'url_listar_cursos': 'listar_cursos'
    }
    return render(request, 'cadastro/pagina_principal.html', contexto)

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

# CADASTRO DE CURSOS
def cadastrar_curso(request) :
    if request.method == 'POST' :
        form = CursoForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('listar_cursos')
    else :
        form = CursoForm()
    return render(request, 'cadastro/cadastrar_curso.html', {'form': form})

# LISTAGEM DOS CURSOS
def listar_cursos(request) :
    cursos = Curso.objects.all()
    return render(request, 'cadastro/listar_cursos.html', {'cursos': cursos})

# DELETE DO CURSO
def excluir_curso(request, curso_id) :
    curso = get_object_or_404(Curso, id = curso_id)
    curso.delete()
    return redirect('listar_cursos')

# EDITAR CURSO
def editar_curso(request, curso_id) :
    curso = get_object_or_404(Curso, id = curso_id)

    if request.method == 'POST' :
        form = CursoForm(request.POST, instance = curso)
        if form.is_valid() :
            form.save()
            return redirect('listar_cursos')
    else :
        form = CursoForm(instance = curso)
    return render(request, 'cadastro/editar_curso.html', {'form': form})