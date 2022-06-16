# Generated by Django 4.0.4 on 2022-06-16 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_productmehtod_alter_ip_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductMehtod',
        ),
        migrations.CreateModel(
            name='ProductMehtod',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
            ],
            bases=('products.product',),
        ),
    ]
