# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-30 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_emailuser_is_social'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='left',
        ),
        migrations.RemoveField(
            model_name='state',
            name='top',
        ),
        migrations.AddField(
            model_name='state',
            name='st',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
