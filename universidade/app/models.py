from django.db import models
import uuid

# Create your models here.
class Universidade(models.Model):
    nome = models.CharField(max_length=100)
    
class Curso(models.Model):
    nome = models.CharField(max_length=30)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nome
    
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nome
    
class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, default=None)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, default=None)
    semestre = models.IntegerField()

    class Meta:
        unique_together = ('aluno', 'semestre')
    