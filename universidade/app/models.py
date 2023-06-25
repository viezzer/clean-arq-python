from datetime import datetime
import pprint

from django.db import models, transaction

import uuid

# Create your models here.
class Universidade(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
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
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=None, null=True)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        self.curso = None
        self.universidade = None
        super().save(using='sensitive_db', *args, **kwargs)



        # print(sexo_sigiloso)
        # super(AlunoSigiloso, .save(using=using_db, *args, **kwargs)


class AlunoSigiloso(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, null=True)
    sexo = models.CharField(max_length=10, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    data_nascimento = models.DateField(null=True)

    def __str__(self):
        return self.aluno.nome

    def save(self, *args, **kwargs):

        local_salario = self.salario
        local_sexo = self.sexo
        local_nasc = self.data_nascimento

        self.salario = None
        self.sexo = None
        self.data_nascimento = None

        super().save(*args, **kwargs)
        self.salario = local_salario
        self.sexo = local_sexo
        self.data_nascimento = local_nasc

        super().save(using='sensitive_db', *args, **kwargs)



class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, default=None)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, default=None)
    semestre = models.IntegerField()

    class Meta:
        unique_together = ('aluno', 'semestre')

    def __str__(self):
        return f"{self.aluno} - {self.disciplina} - {self.semestre} semestre"
