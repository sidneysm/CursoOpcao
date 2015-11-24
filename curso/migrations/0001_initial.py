# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=400)),
                ('data_de_nascimento', models.DateField(blank=True)),
                ('data_de_matricula', models.DateTimeField(null=True, blank=True)),
                ('telefone', models.CharField(null=True, max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Alunos',
                'verbose_name': 'Aluno',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('alunos', models.ManyToManyField(to='curso.Aluno')),
            ],
            options={
                'verbose_name_plural': 'Cursos',
                'verbose_name': 'Curso',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Disciplinas',
                'verbose_name': 'Disciplina',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.IntegerField(null=True)),
                ('endereco', models.CharField(max_length=400)),
                ('data_de_nascimento', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
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
