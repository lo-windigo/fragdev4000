# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('desc', models.TextField(verbose_name='description')),
                ('short_desc', models.CharField(blank=True, max_length=300, verbose_name='short description')),
                ('license', models.CharField(blank=True, max_length=50, verbose_name='code license')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('com', 'Completed'), ('dev', 'In development'), ('prd', 'In Production'), ('hid', 'Hidden')], max_length=3)),
                ('github', models.URLField(blank=True)),
                ('gitlab', models.URLField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('example', models.URLField(blank=True, verbose_name='example URL')),
                ('slug', models.SlugField(max_length=150)),
                ('thumbnail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='images.Image')),
            ],
        ),
    ]
