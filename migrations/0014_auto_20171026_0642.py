# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_emailuser_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number'),
        ),
    ]