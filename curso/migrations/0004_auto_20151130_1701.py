# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_auto_20151128_2300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name': 'Professor', 'verbose_name_plural': 'Professores'},
        ),
    ]
