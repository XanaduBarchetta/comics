# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 19:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ComicCollectionTracker', '0003_defaultcollection'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultcollection',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='defaultcollection',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]