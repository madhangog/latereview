# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-25 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_audience_dbpass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audience',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]