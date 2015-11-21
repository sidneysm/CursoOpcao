# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curso', '0006_auto_20151121_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='cpf',
        ),
        migrations.AddField(
            model_name='aluno',
            name='senha',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, default='', blank=True),
        ),
    ]
