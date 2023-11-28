from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    idade = models.IntegerField()
    curso = models.CharField(max_length=50)
    endereco = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Curso(models.Model) :
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self) :
        return self.nome