# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20171004_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='is active'),
        ),
    ]
