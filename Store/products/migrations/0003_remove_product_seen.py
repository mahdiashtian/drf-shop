# Generated by Django 4.0.4 on 2022-06-16 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_ip_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seen',
        ),
    ]