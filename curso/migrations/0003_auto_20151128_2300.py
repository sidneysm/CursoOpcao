# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_auto_20151128_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disciplina',
            old_name='Professor',
            new_name='professores',
        ),
    ]
