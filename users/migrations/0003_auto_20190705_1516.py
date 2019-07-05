# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-05 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190705_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audience',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='critics',
            name='critic_id',
        ),
        migrations.AlterField(
            model_name='audience',
            name='reviewer_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.reviewer'),
        ),
        migrations.AlterField(
            model_name='critics',
            name='reviewer_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.reviewer'),
        ),
    ]
