# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-25 01:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20170211_1724'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['name']},
        ),
    ]
