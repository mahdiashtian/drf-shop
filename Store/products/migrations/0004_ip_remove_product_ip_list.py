# Generated by Django 4.0.4 on 2022-06-16 09:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_seen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=18), default=list, size=None, verbose_name='ایپی های بازدید کننده از این محصول')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='ip_list',
        ),
    ]