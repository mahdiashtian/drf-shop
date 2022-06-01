from django.contrib import admin
from django.db.models import fields
from .models import Product
from django.contrib import messages
from django import forms
from django.utils.translation import ngettext


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





    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
