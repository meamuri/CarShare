# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 23:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CarShare', '0005_auto_20170119_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelling',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2000, 1, 1, 10, 0)),
        ),
        migrations.AlterField(
            model_name='travelling',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='travelling',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
