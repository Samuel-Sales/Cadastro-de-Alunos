from django.urls import path
from .views import pagina_principal, cadastrar_aluno, lista_alunos, excluir_aluno, detalhes_aluno, atualizar_aluno

urlpatterns = [
    path('', pagina_principal, name = 'pagina_principal'),
    path('alunos/cadastrar/', cadastrar_aluno, name = 'cadastrar_aluno'),
    path('alunos/listar/', lista_alunos, name = 'lista_alunos'),
    path('alunos/excluir/<int:aluno_id>/', excluir_aluno, name = 'excluir_aluno'),
    path('alunos/detalhes/<int:aluno_id>/', detalhes_aluno, name = 'detalhes_aluno'),
    path('alunos/atualizar/<int:aluno_id>/', atualizar_aluno, name = 'atualizar_aluno'),
]