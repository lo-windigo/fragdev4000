# Generated by Django 2.1.7 on 2019-02-24 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='content_type',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]