# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-25 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=12)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False)),
                ('dbpass', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]