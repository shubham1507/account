# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-14 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_appversion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appversion',
            name='version',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
