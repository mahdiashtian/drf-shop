from rest_framework import serializers
from .models import Product
from drf_dynamic_fields import DynamicFieldsMixin


class ProductSerializers(DynamicFieldsMixin,serializers.ModelSerializer):

    def get_category(self,obj):
        category_list = [
            {
                "title":i.title,
                "url":i.get_absolute_url()
             }
             for i in obj.category.all()]
        return category_list


    def get_gallery(self,obj):
        gallery_list = [
            {
                "image":i.image.url
             }
             for i in obj.gallery_product.all()]
        return gallery_list


    url = serializers.CharField(source='get_absolute_url')

    category = serializers.SerializerMethodField('get_category')
    
    gallery = serializers.SerializerMethodField('get_gallery')

    seen = serializers.CharField(source='ip_list')


    class Meta:
        model = Product
        exclude = ('ip',)