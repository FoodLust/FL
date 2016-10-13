# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 04:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_members_activation'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='following',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followers', related_query_name='followers', to='members.Member'),
        ),
    ]