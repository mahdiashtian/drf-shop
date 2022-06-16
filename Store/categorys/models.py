from django.db import models
from rest_framework.reverse import reverse


class Category(models.Model):
    parent = models.ForeignKey('self',on_delete=models.CASCADE,verbose_name="ریشه",default=None,null=True,blank=True,related_name="ch")
    title = models.CharField(max_length=150,verbose_name="عنوان")


    class Meta:
        ordering = ['parent_id']
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


    def get_absolute_url(self):
        pass
        # return reverse("category:Category",kwargs={"category_name":self.name}) 


    def StructureCategory(self):
        return self.title if not self.parent else self.title + " زیر مجموعه : "+self.parent.title


    def __str__(self):
        return self.StructureCategory()