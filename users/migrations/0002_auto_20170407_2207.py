# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-07 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]
