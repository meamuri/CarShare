# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarShare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travelling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_from', models.CharField(max_length=128)),
                ('city_to', models.CharField(max_length=128)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]
