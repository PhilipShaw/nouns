# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20170602_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]
