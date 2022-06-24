from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from categorys.models import Category

class CategorySerializers(DynamicFieldsMixin,serializers.ModelSerializer):

    @staticmethod
    def get_parent(obj):
        return CategorySerializers(obj.category_parent.all(),many=True).data


    url = serializers.CharField(source='get_absolute_url')

    parent = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        
        fields = ['id','title','url','parent']