# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_notification_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
