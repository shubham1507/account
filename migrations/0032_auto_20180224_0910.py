# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-24 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20180214_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailuser',
            name='company_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_country', to='accounts.Country'),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country', to='accounts.Country'),
        ),
    ]
