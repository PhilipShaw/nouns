# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170517_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='noun',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=10, null=True),
        ),
    ]