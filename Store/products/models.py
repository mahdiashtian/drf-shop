from django.db import models
import os
from django.utils.html import format_html


def get_file_name(file_name):
    base_name = os.path.basename(file_name)
    name,ext = os.path.splitext(base_name)
    return name,ext


def upload_image_path(instance,filename):
    name,ext = get_file_name(filename)
    final_name = f"{instance.id}{instance.title}{ext}"
    return f"products/product/{final_name}"


class Product(models.Model):


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
    visit_count = models.IntegerField(default=0,verbose_name='تعداد بازدید',editable=False)





    class Meta:
        app_label = "products"
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        base_manager_name = "objects"
        ordering = ['title','active']
        permissions = [("can_change_price","Can change price")]


<<<<<<< HEAD
    # def get_absolute_url(self):
    #     return reverse("products:ProductDetail", kwargs={"pk": self.id, 'name' : self.title.replace(' ','-')})  # دریافت مقدار از url
=======
#     def get_absolute_url(self):
#         return reverse("products:ProductDetail", kwargs={"pk": self.id, 'name' : self.title.replace(' ','-')})  # دریافت مقدار از url
>>>>>>> cafea4c81668b0b792d834f2c329e1da81e774d1


    def image_admin(self):
        return format_html(f"<img width=40 heigth=30 src={self.image.url}> ")


    image_admin.short_description = "تصویر"



    def __str__(self):
        return self.title

# Create your models here.
