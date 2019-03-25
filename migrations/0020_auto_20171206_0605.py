# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20171206_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]