# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-27 17:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drivers',
            new_name='Driver',
        ),
    ]
