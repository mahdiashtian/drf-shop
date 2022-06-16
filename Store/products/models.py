from django.db import models
import os
from django.utils.html import format_html
from categorys.models import Category
from rest_framework.reverse import reverse
from django.contrib.postgres.fields import ArrayField


def get_file_name(file_name):
    base_name = os.path.basename(file_name)
    name,ext = os.path.splitext(base_name)
    return name,ext


def upload_image_path(instance,filename):
    name,ext = get_file_name(filename)
    final_name = f"{instance.id}{instance.title}{ext}"
    return f"products/product/{final_name}"


class Ip(models.Model):
    ip_list = ArrayField(
            models.CharField(max_length=18, blank=True),default=list,verbose_name='ایپی های بازدید کننده از این محصول'
    )

    
    # def ReturnView(self):
        # print(self.ip_list)


    class Meta:
        abstract = True


class Product(Ip):
    userdefined_error_msg = {
        'max_length': 'حداثر 150 حرف',
        'blank': 'این فیلد نمی تواند خالی باشد'
    }

    title = models.CharField(
        verbose_name='عنوان',
        max_length=150,
        blank=False,
        help_text="اسم محصول",
        error_messages=userdefined_error_msg
    )
    
    description = models.TextField(verbose_name='توضیحات')
    
    price = models.IntegerField(verbose_name='قیمت')
    
    image = models.ImageField(upload_to=upload_image_path,null=True,blank=True,verbose_name='تصویر')
    
    active = models.BooleanField(default=False,verbose_name='وضعیت فعالیت محصول')
       
    is_slider = models.BooleanField(default=False,verbose_name='استفاده به عنوان اسلایدر')

    category = models.ManyToManyField(Category,blank=True,verbose_name="دسته بندی ها")


    class Meta:
        app_label = "products"
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        base_manager_name = "objects"
        ordering = ['title','active']
        permissions = [("can_change_price","Can change price")]


    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"pk": self.id})


    def image_admin(self):
        return format_html(f"<img width=40 heigth=30 src={self.image.url}> ")


    image_admin.short_description = "تصویر"


    def __str__(self):
        return self.title