# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-05 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direction_options', '0002_directionoption_shuttle_station_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directionoption',
            name='shuttle_station_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='direction_options', to='shuttle_stations.ShuttleStation'),
        ),
    ]