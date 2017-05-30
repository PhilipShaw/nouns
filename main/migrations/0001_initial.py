# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 22:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Noun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=200, null=True)),
                ('item_type', models.CharField(max_length=50, null=True)),
                ('rating_guess', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('create_for', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NounScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_score', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.Noun')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]