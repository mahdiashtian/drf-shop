from rest_framework import serializers
from orders.models import Order , OrderDetail
from drf_dynamic_fields import DynamicFieldsMixin


class OrderDetailSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    
    def validate(self,data):
        user = self.context['request'].user
        data['order'],reuslt = Order.objects.get_or_create(user=user,is_paid=False)
        return data


    def validate_product(self,value):
        user = self.context['request'].user
        if OrderDetail.objects.filter(order__is_paid=False,order__user=user,product=value).exists():
            raise serializers.ValidationError('شما از قبل این محصول را در سبد خرید خود دارید')
        return value

    product_title = serializers.ReadOnlyField(source='product.title')

    price = serializers.ReadOnlyField(source='product.price')

    url = serializers.ReadOnlyField(source='get_absolute_url')

    class Meta:
        model = OrderDetail
        fields = [
            'id',
            'product_title',
            'product',
            'price',
            'order',
            'count',
            'url',
            ]

        read_only_fields = [
            'price',
            'order',
        ]


class OrderSerializer(serializers.ModelSerializer):

    url = serializers.ReadOnlyField(source='get_absolute_url')

    class Meta:
        model = Order
        fields = [
            'id',
            'is_paid',
            'date_paid',
            'url',
            'user',
        ]