from django.db import models
import os
from django.urls import reverse
from django.db.models import Q
from products.models import Product
from .utils import upload_galleries_image_path


class ProductGallery(models.Model):
    image = models.ImageField(upload_to=upload_galleries_image_path, verbose_name='تصویر')
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='gallery',related_query_name='gallery_Q')


    class Meta:
        verbose_name = 'تصویر محصولات'
        verbose_name_plural = 'تصاویر محصولات'


    def __str__(self):
        return self.product.title




