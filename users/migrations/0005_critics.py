# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-29 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190625_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Critics',
            fields=[
                ('critic_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_critic', models.BooleanField(default=True)),
            ],
        ),
    ]