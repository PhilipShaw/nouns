# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 02:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nounscore',
            old_name='user',
            new_name='noun',
        ),
    ]
