# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AddField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'name', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'name', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'name', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'name', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'name', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offering',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'name', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='state',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'name', blank=True, unique=True),
            preserve_default=True,
        ),
    ]
