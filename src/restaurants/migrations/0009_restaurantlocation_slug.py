# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20171107_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
