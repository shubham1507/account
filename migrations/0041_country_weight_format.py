# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-28 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_auto_20180310_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='weight_format',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]