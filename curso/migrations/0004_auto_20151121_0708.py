# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_remove_professor_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='matriculado',
            new_name='ativo',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='matriculado',
        ),
    ]
