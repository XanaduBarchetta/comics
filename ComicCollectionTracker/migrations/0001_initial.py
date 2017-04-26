# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comicvine_id', models.CharField(max_length=100)),
                ('publication', models.CharField(max_length=300)),
                ('printing', models.CharField(default='1', max_length=100)),
                ('cover', models.CharField(max_length=100, verbose_name='Cover number or letter')),
                ('cover_url', models.CharField(max_length=500)),
                ('issue_comment', models.TextField(default=None)),
                ('own_physical', models.BooleanField(default=False)),
                ('own_digital', models.BooleanField(default=False)),
                ('have_read', models.BooleanField(default=False)),
                ('collection_comment', models.TextField(default=None)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComicCollectionTracker.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComicCollectionTracker.User'),
        ),
    ]
