from django.db import models


def get_file_name(file_name):
    base_name = os.path.basename(file_name)
    name,ext = os.path.splitext(base_name)
    return name,ext


def upload_image_path(instance,filename):
    name,ext = get_file_name(filename)
    final_name = f"{instance.id}{instance.title}{ext}"
    return f"products/{final_name}"


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
    visit_count = models.IntegerField(default=0,verbose_name='تعداد بازدید')


    class Meta:
        app_label = "products"
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        base_manager_name = "objects"
        ordering = ['title','active']
        permissions = [("can_read_price","Can read price")]


    def get_absolute_url(self):
        return reverse("products:ProductDetail", kwargs={"pk": self.id, 'name' : self.title.replace(' ','-')})  # دریافت مقدار از url


    def image_admin(self):
        return format_html(f"<img width=40 heigth=30 src={self.image.url}> ")


    image_admin.short_description = "تصویر"



    def __str__(self):
        return self.title

# Create your models here.
