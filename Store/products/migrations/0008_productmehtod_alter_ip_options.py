# Generated by Django 4.0.4 on 2022-06-16 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_ip_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMehtod',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('products.product',),
        ),
        migrations.AlterModelOptions(
            name='ip',
            options={'base_manager_name': 'objects', 'ordering': ['id'], 'verbose_name': 'آیپی', 'verbose_name_plural': 'آیپی ها'},
        ),
    ]