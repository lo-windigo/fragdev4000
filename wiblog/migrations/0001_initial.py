# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('name', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now=True)),
                ('moderated', models.CharField(choices=[('HAM', 'Valid'), ('SPM', 'Invalid (Spam)'), ('UNK', 'Unmoderated')], default='UNK', max_length=14)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=150)),
                ('status', models.CharField(choices=[('DFT', 'Draft'), ('PUB', 'Published')], max_length=9)),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=50, unique=True, verbose_name='Tag')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='wiblog.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiblog.Post'),
        ),
    ]
