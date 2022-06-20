from rest_framework import serializers
from .models import Category
from drf_dynamic_fields import DynamicFieldsMixin
from products.serializer_ import ProductSerializers

class CategorySerializers(DynamicFieldsMixin,serializers.ModelSerializer):

    @staticmethod
    def get_parent(obj):
        return CategorySerializers(obj.category_parent.all(),many=True).data


    url = serializers.CharField(source='get_absolute_url')

    parent = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = '__all__'