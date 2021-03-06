# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-02-26 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockID', models.IntegerField(default='null', max_length=11)),
                ('blockName', models.CharField(default='null', max_length=255)),
                ('parameterUserName', models.CharField(default='null', max_length=255)),
                ('displayOrder', models.IntegerField(default='null', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planeID', models.CharField(default='null', max_length=255)),
                ('username', models.CharField(default='null', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='test_data',
            fields=[
                ('id', models.IntegerField(default='null', primary_key=True, serialize=False)),
                ('blocknum', models.IntegerField(default='1', max_length=255)),
                ('data', models.CharField(default='null', max_length=1024)),
                ('MD5', models.CharField(default='null', max_length=256)),
            ],
        ),
    ]
