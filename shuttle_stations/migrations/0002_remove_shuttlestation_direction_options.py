# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-05 11:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle_stations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shuttlestation',
            name='direction_options',
        ),
    ]
