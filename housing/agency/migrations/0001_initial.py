# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 16:49
from __future__ import unicode_literals

import agency.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=agency.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=100)),
                ('width_field', models.IntegerField(default=100)),
                ('name', models.CharField(max_length=140)),
                ('slug', models.SlugField(unique=True)),
                ('location', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('bedrooms', models.IntegerField()),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
