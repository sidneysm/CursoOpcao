# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curso', '0007_auto_20151121_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='senha',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AddField(
            model_name='professor',
            name='usuario',
            field=models.ForeignKey(editable=False, blank=True, default='', to=settings.AUTH_USER_MODEL),
        ),
    ]
