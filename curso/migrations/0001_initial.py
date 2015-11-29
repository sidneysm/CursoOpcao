# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=14)),
                ('endereco', models.CharField(max_length=400)),
                ('data_de_nascimento', models.DateField(blank=True)),
                ('data_de_matricula', models.DateTimeField(null=True, blank=True)),
                ('telefone', models.CharField(max_length=20)),
                ('situacao', models.CharField(default='Pagamento não efetuado', max_length=10)),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(null=True)),
                ('duracao', models.IntegerField(null=True)),
                ('data_de_inicio', models.DateField(null=True)),
                ('alunos', models.ManyToManyField(to='curso.Aluno', blank=True)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('user_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=14)),
                ('endereco', models.CharField(max_length=400)),
                ('data_de_nascimento', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='disciplina',
            name='Professor',
            field=models.ManyToManyField(to='curso.Professor'),
        ),
        migrations.AddField(
            model_name='curso',
            name='disciplinas',
            field=models.ManyToManyField(to='curso.Disciplina'),
        ),
    ]
