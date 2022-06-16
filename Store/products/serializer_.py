from weakref import proxy
from coreapi import Link
from numpy import source
from rest_framework import serializers
from .models import Product
from drf_dynamic_fields import DynamicFieldsMixin


class ProductSerializers(DynamicFieldsMixin,serializers.ModelSerializer):

    url = serializers.CharField(source='get_absolute_url')

    def get_title(self,obj):
        category_list = [
            {
                "title":i.title,
                "url":i.get_absolute_url()
             }
             for i in obj.category.all()]
        return category_list


    category = serializers.SerializerMethodField('get_title')
    
    seen = serializers.CharField(source='ip_list')
 

    class Meta:
        model = Product
        exclude = ('ip',)