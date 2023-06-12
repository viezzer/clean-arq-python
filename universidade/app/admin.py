from django.contrib import admin
from .models import Universidade, Curso, Disciplina, Aluno, Matricula

# Register your models here.
admin.site.register(Universidade)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Aluno)
admin.site.register(Matricula)