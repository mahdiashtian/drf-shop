# Generated by Django 4.0.4 on 2022-06-16 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
