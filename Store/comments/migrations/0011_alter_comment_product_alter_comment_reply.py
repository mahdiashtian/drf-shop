# Generated by Django 4.0.4 on 2022-06-09 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_is_slider'),
        ('comments', '0010_alter_comment_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_c', to='comments.comment', verbose_name='ریپلای'),
        ),
    ]
