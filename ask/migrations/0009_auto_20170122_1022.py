# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 04:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0008_auto_20170122_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='score',
            new_name='popularity',
        ),
    ]