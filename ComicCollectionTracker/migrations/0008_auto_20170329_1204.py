# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-29 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComicCollectionTracker', '0007_auto_20170327_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='comicvine_id',
            field=models.IntegerField(max_length=15),
        ),
    ]
