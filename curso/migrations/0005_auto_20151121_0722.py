# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0004_auto_20151121_0708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='curso',
        ),
        migrations.AddField(
            model_name='curso',
            name='alunos',
            field=models.ManyToManyField(to='curso.Aluno'),
        ),
    ]
