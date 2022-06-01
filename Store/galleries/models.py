from django.db import models
import os
from django.urls import reverse
from django.db.models import Q
from products.models import Product


def get_file_name(file_name):
    base_name = os.path.basename(file_name)
    name,ext = os.path.splitext(base_name)
    return name[0:5],ext


def upload_galleries_image_path(instance,filename):
    instance = instance.product
    name,ext = get_file_name(filename)
    final_name = f"{instance.title}-{name}-{ext}"
    return f"products/gallerie/{instance.id}/{final_name}"


class ProductGallery(models.Model):
    image = models.ImageField(upload_to=upload_galleries_image_path, verbose_name='تصویر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='gallery',related_query_name='gallery_Q')


    class Meta:
        verbose_name = 'تصویر محصولات'
        verbose_name_plural = 'تصاویر محصولات'


    def __str__(self):
        return self.product.title




