from rest_framework.generics import ListAPIView , RetrieveAPIView
from .serializer_ import ProductSerializers
from .models import Product
from rest_framework import viewsets
from django_filters import rest_framework as filters


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')


    class Meta:
        model = Product
        fields = ['active']


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    http_method_names = ['get']
    filterset_class = ProductFilter
    search_fields = ['title']
    ordering_fields = ['id']


    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset


