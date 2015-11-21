# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curso', '0002_auto_20151121_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='usuario',
            field=models.OneToOneField(null=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
