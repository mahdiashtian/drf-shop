# Generated by Django 4.0.4 on 2022-06-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_product_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(help_text='اسم محصول', max_length=150, verbose_name='عنوان'),
        ),
    ]
