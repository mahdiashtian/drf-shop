from coreapi import Link
from numpy import source
from rest_framework import serializers
from .models import Product


class CategoryProduct(serializers.RelatedField):
    def to_representation(self, value):
        return value.StructureCategory()


class ProductSerializers(serializers.ModelSerializer):
    # روش های مختلف نشان دادن لینک {
    url = serializers.HyperlinkedIdentityField(view_name='products:product-detail')
    # url = serializers.StringRelatedField(source='get_absolute_url')
    # url = serializers.CharField(source='get_absolute_url')
    # }


    # روش های مختلف نشان دادن دسته بندی ها {
    category = CategoryProduct(read_only=True,many=True)
    # def get_title(self,obj):
    #     category_list = [i.StructureCategory() for i in obj.category.all()]
    #     return category_list


    # category = serializers.SerializerMethodField('get_title')
    # }

    class Meta:
        model = Product
        fields = '__all__'