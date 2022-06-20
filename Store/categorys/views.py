from unicodedata import category
from products.serializer_ import ProductSerializers
from .serializer_ import CategorySerializers
from .models import Category
from rest_framework import viewsets
from products.models import Product

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'category'
    lookup_url_kwarg = 'pk'
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

    def get_queryset(self):
        if self.action == 'list':
            queryset = Category.objects.all()
        else:
            queryset = Product.objects.all()
        return queryset
    

    def get_serializer_class(self):
        if self.action == 'list':
            serializer_class = CategorySerializers
        else:
            serializer_class = ProductSerializers
        return serializer_class
    