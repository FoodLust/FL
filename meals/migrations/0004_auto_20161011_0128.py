# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 01:28
from __future__ import unicode_literals

from django.db import migrations, models
import meals.models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_auto_20161011_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='photo',
            field=models.ImageField(upload_to=meals.models.upload_directory_path),
        ),
    ]
