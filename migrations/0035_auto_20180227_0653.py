# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-27 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_auto_20180224_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
