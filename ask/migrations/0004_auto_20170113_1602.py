# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0003_question_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.CharField(default=b'anon', max_length=100),
        ),
    ]