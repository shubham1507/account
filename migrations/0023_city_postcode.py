# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-13 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20171209_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='postcode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]