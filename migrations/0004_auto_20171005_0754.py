# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20171005_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailuser',
            name='company_logo',
            field=models.ImageField(blank=True, null=True, upload_to='CompanyLogo/'),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='UserImages/'),
        ),
    ]
