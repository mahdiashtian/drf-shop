from rest_framework.generics import ListAPIView , RetrieveAPIView
from .serializer_ import ProductSerializers
from .models import Product
from rest_framework import viewsets
from .filters import ProductFilter


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


