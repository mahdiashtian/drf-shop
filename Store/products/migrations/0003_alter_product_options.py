# Generated by Django 4.0.4 on 2022-05-30 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'base_manager_name': 'objects', 'ordering': ['title', 'active'], 'permissions': [('can_read_price', 'Can read price')], 'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
    ]
