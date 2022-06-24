from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse


User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name="پرداخت شده / نشده",default=False)
    date_paid = models.DateTimeField(blank=True,null=True,verbose_name="تاریخ پرداخت")

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد های خرید کاربران"


    def get_absolute_url(self):
        return reverse("orders:order-dt-list", kwargs={"id": self.pk})
    

    def __str__(self):
        return self.user.username


class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="سبد خرید")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="محصول")
    price = models.IntegerField(verbose_name="قیمت محصول",blank=True,null=True)
    count = models.PositiveIntegerField(verbose_name="تعداد")

    class Meta:
        verbose_name = "جزییات محصول"
        verbose_name_plural = "اطلاعات جزییات محصولات"


    def get_absolute_url(self):
        return reverse("orders:order-dt-detail", kwargs={"id":self.order.id,"pk": self.pk})


    def __str__(self):
        return self.product.title


