# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-08 06:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_auto_20180308_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='group_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.GroupCountry'),
        ),
    ]