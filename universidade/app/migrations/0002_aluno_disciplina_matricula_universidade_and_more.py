# Generated by Django 4.2.2 on 2023-06-08 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.IntegerField()),
                ('aluno', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.aluno')),
                ('disciplina', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
            ],
            options={
                'unique_together': {('aluno', 'semestre')},
            },
        ),
        migrations.CreateModel(
            name='Universidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Estudante',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='codigo',
        ),
        migrations.AddField(
            model_name='curso',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disciplina',
            name='curso',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.curso'),
        ),
        migrations.AddField(
            model_name='curso',
            name='universidade',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.universidade'),
        ),
    ]