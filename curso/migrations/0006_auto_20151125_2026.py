# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0005_auto_20151124_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='descricao',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='alunos',
            field=models.ManyToManyField(to='curso.Aluno', blank=True),
        ),
    ]
