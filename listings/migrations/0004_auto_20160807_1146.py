# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20160801_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetroArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'name', blank=True, unique=True)),
                ('state', models.ForeignKey(to='listings.State')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='metroarea',
            field=models.ForeignKey(to='listings.MetroArea', null=True),
            preserve_default=True,
        ),
    ]
