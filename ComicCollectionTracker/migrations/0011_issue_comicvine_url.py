# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-29 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComicCollectionTracker', '0010_remove_issue_comicvine_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='comicvine_url',
            field=models.CharField(default=None, max_length=500),
        ),
    ]