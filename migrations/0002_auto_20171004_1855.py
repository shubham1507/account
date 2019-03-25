# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='City Name')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Country Name')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='State Name')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Country')),
            ],
        ),
        migrations.AddField(
            model_name='emailuser',
            name='ABN',
            field=models.CharField(blank=True, max_length=200, verbose_name='ABN'),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='address_line_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='address_line_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='company_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='Company Name'),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='is_buyer',
            field=models.BooleanField(default=False, verbose_name='is buyer'),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='is_notification_sound',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='is_notification_vibrate',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='is_seller',
            field=models.BooleanField(default=True, verbose_name='is seller'),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='profile_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.State'),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.City'),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Country'),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.State'),
        ),
    ]
