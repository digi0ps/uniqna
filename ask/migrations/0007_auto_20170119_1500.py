# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0006_auto_20170118_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
