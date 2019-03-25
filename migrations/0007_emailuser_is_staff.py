# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_emailuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
