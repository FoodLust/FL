# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 00:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meals', '0002_auto_20161010_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='meals.Meal')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='ratting',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='ratting',
            name='member',
        ),
        migrations.DeleteModel(
            name='Ratting',
        ),
    ]