# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='data_de_inicio',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='duracao',
            field=models.IntegerField(null=True),
        ),
    ]
