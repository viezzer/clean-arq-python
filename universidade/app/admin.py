from django.contrib import admin
from django import forms
from .models import Universidade, Curso, Disciplina, Aluno, Matricula

# Register your models here.
# class UniversidadeForm(forms.ModelForm):
#     class Meta:
#         model = Universidade
#         fields = '__all__'

#     def clean(self):
#         cleaned_data = super().clean()
#         cursos_count = Curso.objects.filter(universidade=cleaned_data.get('universidade')).count()
#         if cursos_count < 3:
#             raise forms.ValidationError('Uma Universidade deve ter no mínimo três cursos cadastrados.')

# class UniversidadeAdmin(admin.ModelAdmin):
#     form = UniversidadeForm

# class CursoAdminForm(forms.ModelForm):
#     class Meta:
#         model = Curso
#         fields = '__all__'

#     def clean(self):
#         cleaned_data = super().clean()
#         disciplinas = cleaned_data.get('disciplinas')
#         if disciplinas and len(disciplinas) < 10:
#             raise forms.ValidationError('Um Curso deve ter pelo menos dez disciplinas cadastradas.')
#         alunos = cleaned_data.get('alunos')

# class CursoAdmin(admin.ModelAdmin):
#     form = CursoAdminForm

class UniversidadeForm(forms.ModelForm):
    class Meta:
        model = Universidade
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        cursos_count = cleaned_data.get('cursos').count()

        if cursos_count < 3:
            raise forms.ValidationError('Uma Universidade deve ter no mínimo três cursos cadastrados.')


class CursoInlineFormSet(admin.StackedInline):
    model = Curso
    def clean(self):
        super().clean()
        total_forms = self.total_form_count()

        if total_forms < 10:
            raise forms.ValidationError('Um Curso deve ter no mínimo dez disciplinas cadastradas.')


class AlunoInlineFormSet(admin.StackedInline):
    model = Aluno
    
    def clean(self):
        super().clean()
        total_forms = self.total_form_count()

        if total_forms < 5:
            raise forms.ValidationError('Um Curso deve ter no mínimo cinco alunos cadastrados.')


class UniversidadeAdmin(admin.ModelAdmin):
    form = UniversidadeForm
    inlines = [
        CursoInlineFormSet,
        AlunoInlineFormSet,
    ]


admin.site.register(Universidade, UniversidadeAdmin)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Aluno)
admin.site.register(Matricula)