# Generated by Django 4.0.4 on 2022-06-16 08:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ip_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=18), default=list, size=None, verbose_name='ایپی های بازدید کننده از این محصول'),
        ),
    ]