# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(null=True, upload_to=b'listings', blank=True)),
                ('website', models.CharField(max_length=500, null=True, blank=True)),
                ('address_1', models.CharField(max_length=500, null=True, blank=True)),
                ('address_2', models.CharField(max_length=500, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('categories', models.ManyToManyField(to='listings.Category')),
                ('city', models.ForeignKey(to='listings.City', null=True)),
                ('country', models.ForeignKey(to='listings.Country', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('city', models.ForeignKey(to='listings.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='listing',
            name='neighborhood',
            field=models.ForeignKey(to='listings.Neighborhood', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='offerings',
            field=models.ManyToManyField(to='listings.Offering', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.ForeignKey(to='listings.State', null=True),
            preserve_default=True,
        ),
    ]
