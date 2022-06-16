from .serializer_ import CategorySerializers
from .models import Category
from rest_framework import generics
from rest_framework.filters import SearchFilter
from products.models import Product
from products.serializer_ import ProductSerializers


class CategoryListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerializers
    search_fields = ['title']
    filter_backends = [SearchFilter]


    def get_queryset(self):
        queryset = Category.objects.filter(parent=None)
        return queryset


class CategoryRetrieveView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ProductSerializers


    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Product.objects.filter(category=pk)
        return queryset

