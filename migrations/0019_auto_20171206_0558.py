# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20171206_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailuser',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Superuser status'),
        ),
    ]