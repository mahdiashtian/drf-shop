from django.db import models




class Comment(models.Model):    
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE,verbose_name='محصول')
    
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='کاربر')
    
    date_time_added = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت')
    
    date_time_edit = models.DateTimeField(auto_now=True,verbose_name='تاریخ اصلاح')
    
    confirmation = models.BooleanField(default=False,verbose_name='تایید شده/نشده')

    main_message = models.CharField(max_length=150,verbose_name='کامنت')

    class Meta:
        app_label = "comments"
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        base_manager_name = "objects"
        ordering = ['date_time_added','date_time_edit']
        

    def __str__(self):
        return self.product.title


