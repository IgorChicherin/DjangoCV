# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='img',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
    ]
