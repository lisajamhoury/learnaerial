# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-27 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20170726_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='code',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]