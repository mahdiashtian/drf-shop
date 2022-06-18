from rest_framework import serializers
from .models import Category
from drf_dynamic_fields import DynamicFieldsMixin


class CategorySerializers(DynamicFieldsMixin,serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url')
    def get_parent(self,obj):
        category_list = [
            {
                "id":i.id,
                "title":i.title,
                "url":i.get_absolute_url()
             }
             for i in obj.category_parent.all()]
        return category_list


    parent = serializers.SerializerMethodField('get_parent')
    

    class Meta:
        model = Category
        fields = '__all__'