# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0007_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
    ]
