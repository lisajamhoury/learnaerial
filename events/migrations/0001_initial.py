# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.BooleanField(default=False)),
                ('ongoing', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to=b'events', blank=True)),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField()),
                ('venue', models.CharField(max_length=500)),
                ('venue_url', models.CharField(max_length=500, null=True, blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('time', models.CharField(max_length=500, null=True, blank=True)),
                ('price', models.CharField(max_length=500, null=True, blank=True)),
                ('link', models.CharField(max_length=500, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
