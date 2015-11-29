# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='situacao',
            field=models.CharField(max_length=50, default='Pagamento não efetuado'),
        ),
    ]
