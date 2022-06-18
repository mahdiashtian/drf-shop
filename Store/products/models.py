from weakref import proxy
from django.db import models
from categorys.models import Category
from rest_framework.reverse import reverse
from django.contrib.postgres.fields import ArrayField
from utils.utils import upload_image_path


class Ip(models.Model):
    title = models.CharField(max_length=150,blank=True,null=True)
    ip_list = ArrayField(
            models.CharField(max_length=18, blank=True),default=list,verbose_name='ایپی های بازدید کننده از این محصول'
    )


    class Meta:
        app_label = "products"
        verbose_name = 'آیپی'
        verbose_name_plural = 'آیپی ها'
        base_manager_name = "objects"
        ordering = ['id']


    def __str__(self):
        return f"{self.title} - {self.id}"


class Product(models.Model):
    title = models.CharField(
        verbose_name='عنوان',
        max_length=150,
        blank=False,
        help_text="اسم محصول",
    )
    
    description = models.TextField(verbose_name='توضیحات')
    
    price = models.IntegerField(verbose_name='قیمت')

    image = models.ImageField(upload_to=upload_image_path,null=True,blank=True,verbose_name='تصویر')
    
    active = models.BooleanField(default=False,verbose_name='وضعیت فعالیت محصول')
       
    is_slider = models.BooleanField(default=False,verbose_name='استفاده به عنوان اسلایدر')

    category = models.ManyToManyField(Category,blank=True,verbose_name="دسته بندی ها",related_name='product_category')

    ip = models.OneToOneField(Ip,on_delete=models.SET_NULL,blank=True,null=True,related_name='product_ip')


    class Meta:
        app_label = "products"
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        base_manager_name = "objects"
        ordering = ['title','active']
        permissions = [("can_change_price","Can change price")]


    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"pk": self.id})
        

    def ip_list(self):
        return len(self.ip.ip_list)


    def get_gallery(self):
        pass


    def __str__(self):
        return self.title
