# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_remove_aluno_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='alunos',
            field=models.ManyToManyField(to='curso.Aluno', null=True),
        ),
    ]
