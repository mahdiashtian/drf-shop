from django.db import models


class Comment(models.Model):    
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE,verbose_name='محصول',null=True,blank=True)
    
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='کاربر')
    
    date_time_added = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت')
    
    confirmation = models.BooleanField(default=False,verbose_name='تایید شده/نشده')

    main_message = models.CharField(max_length=150,verbose_name='کامنت')

    reply = models.ForeignKey('comments.Comment',on_delete=models.CASCADE,related_name='comment_reply',verbose_name='ریپلای',null=True,blank=True)


    class Meta:
        app_label = "comments"
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        base_manager_name = "objects"
        ordering = ['-reply_id']
        

    def __str__(self):
        return f'{self.user.username}-:-{self.main_message}'