# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-27 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0009_experiment_addon_versions'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='dashboard_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
