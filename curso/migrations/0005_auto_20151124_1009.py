# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0004_auto_20151124_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='alunos',
            field=models.ManyToManyField(null=True, to='curso.Aluno', blank=True),
        ),
    ]
