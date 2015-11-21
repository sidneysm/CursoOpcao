# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('matricula', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.IntegerField()),
                ('endereco', models.CharField(max_length=400)),
                ('data_de_nascimento', models.DateTimeField(blank=True)),
                ('matriculado', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.IntegerField()),
                ('endereco', models.CharField(max_length=400)),
                ('data_de_nascimento', models.DateTimeField(blank=True)),
                ('matriculado', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
                ('curso', models.ManyToManyField(to='curso.Curso')),
                ('disciplinas', models.ManyToManyField(to='curso.Disciplina')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professor',
            },
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(to='curso.Curso'),
        ),
    ]
