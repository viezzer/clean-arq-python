from django.db import models
import uuid

# Create your models here.
class Estudante(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_lenght=30)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=30)