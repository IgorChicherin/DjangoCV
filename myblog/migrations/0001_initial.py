# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=150)),
                ('phonenum', models.IntegerField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('course', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('tag', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('work_name', models.CharField(max_length=100)),
                ('link', models.URLField(max_length=250, null=True)),
                ('text', models.TextField()),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=150)),
                ('link', models.URLField(max_length=250)),
                ('text', models.TextField()),
                ('date', models.CharField(max_length=200)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myblog.Company')),
            ],
        ),
    ]
