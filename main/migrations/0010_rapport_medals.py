# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20170524_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='rapport',
            name='medals',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
