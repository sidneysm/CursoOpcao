# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0010_auto_20151121_2350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name': 'Professor', 'verbose_name_plural': 'Professores'},
        ),
        migrations.AlterField(
            model_name='professor',
            name='usuario',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, null=True, blank=True, default=''),
        ),
    ]
