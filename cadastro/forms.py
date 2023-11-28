from django import forms
from .models import Aluno, Curso

class AlunoForm(forms.ModelForm) :
    class Meta :
        model = Aluno
        fields = ['nome', 'matricula', 'idade', 'curso', 'endereco', 'email']

class CursoForm(forms.ModelForm) :
    class Meta :
        model = Curso
        fields = ['nome', 'descricao']