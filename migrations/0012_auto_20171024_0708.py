# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20171016_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailuser',
            name='is_seller',
            field=models.BooleanField(default=False, verbose_name='is seller'),
        ),
    ]
