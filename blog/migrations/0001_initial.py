# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0002_auto_20170211_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('order', models.IntegerField(default=0)),
                ('page_title', models.CharField(blank=True, max_length=200)),
                ('meta_description', models.TextField(blank=True)),
                ('body', models.TextField(blank=True, verbose_name='Post Content')),
                ('summary', models.TextField(blank=True, verbose_name='Post Summary')),
                ('published', models.BooleanField(default=False)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('thumbnail_image', models.ImageField(blank=True, null=True, upload_to='blog/thumbnails')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='blog/banner')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
                ('categories', models.ManyToManyField(blank=True, to='blog.Category')),
                ('listings', models.ManyToManyField(blank=True, to='listings.Listing')),
                ('related_posts', models.ManyToManyField(blank=True, to='blog.Post')),
            ],
            options={
                'ordering': ['order', '-publish_date'],
            },
        ),
    ]
