# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-05 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0005_auto_20210304_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]