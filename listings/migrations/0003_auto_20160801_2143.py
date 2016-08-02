# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20150723_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='listings.State', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='neighborhood',
            field=models.ForeignKey(blank=True, to='listings.Neighborhood', null=True),
            preserve_default=True,
        ),
    ]
