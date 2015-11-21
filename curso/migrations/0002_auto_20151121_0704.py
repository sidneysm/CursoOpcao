# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='disciplinas',
        ),
        migrations.AddField(
            model_name='curso',
            name='disciplinas',
            field=models.ManyToManyField(to='curso.Disciplina'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='Professor',
            field=models.ManyToManyField(to='curso.Professor'),
        ),
    ]
