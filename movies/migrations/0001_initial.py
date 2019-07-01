# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-30 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movies_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, unique=True)),
                ('director', models.CharField(max_length=15)),
                ('writer', models.CharField(max_length=15)),
                ('music', models.CharField(max_length=30)),
                ('cast', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=15)),
            ],
        ),
    ]
