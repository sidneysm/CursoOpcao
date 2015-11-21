# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0005_auto_20151121_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='data_de_matricula',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_de_nascimento',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='data_de_nascimento',
            field=models.DateField(blank=True),
        ),
    ]
