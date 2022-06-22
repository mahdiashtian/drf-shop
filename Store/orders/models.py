from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse


User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product,verbose_name="محصول",related_name='orderdetail_product')
    price = models.IntegerField(verbose_name="قیمت محصول",null=True,blank=True)
    is_paid = models.BooleanField(verbose_name="پرداخت شده / نشده",default=False)
    date_paid = models.DateTimeField(blank=True,null=True,verbose_name="تاریخ پرداخت")

    class Meta:
        app_label = "orders"
        verbose_name = "جزییات محصول"
        verbose_name_plural = "اطلاعات جزییات محصولات"

    def get_price(self):
        return self.product.price


    def get_total_price(self):
        return self.get_price * self.count


    def get_absolute_url(self):
        return reverse("orders:order-detail",kwargs={"pk":self.id})


    def __str__(self):
        return self.product.title

