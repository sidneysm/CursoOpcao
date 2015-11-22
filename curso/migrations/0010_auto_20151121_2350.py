# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0009_auto_20151121_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='usuario',
            field=models.ForeignKey(blank=True, default='', editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
