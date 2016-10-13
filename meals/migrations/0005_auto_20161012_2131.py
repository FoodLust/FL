# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_auto_20161011_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='title',
            field=models.CharField(max_length=24, verbose_name='Title'),
        ),
    ]