# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0004_auto_20151130_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='matriculado',
            field=models.BooleanField(default=False),
        ),
    ]
