from django.contrib import admin
from .models import Product,Ip
from django import forms
from django.utils.translation import ngettext
from django.utils.html import format_html


class EventForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['price',]


class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_admin', 'description', 'price', 'active')  # نمایش سر تیتر
    search_fields = ['teitle']


    def get_form(self, request, obj=None, **kwargs):
        if request.user.has_perm("products.can_change_price"):
            form = EventAdminForm
        else:
            form = EventForm
        return form


    @admin.display(description='تصویر')
    def image_admin(self,obj):
        if obj.image:
            return format_html(f"<img width=40 heigth=30 src={obj.image.url}> ")
        return ""


    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Ip)