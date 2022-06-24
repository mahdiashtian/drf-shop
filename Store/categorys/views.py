from .serializers_ import CategorySerializers 
from products.serializers_ import ProductSerializers
from .models import Category
from rest_framework import viewsets , mixins
from products.models import Product
from rest_framework.decorators import action
from rest_framework.response import Response


class CategoryViewSet(mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = CategorySerializers


    @action(detail=True, methods=['get'])
    def list_product(self, request, pk=None):
        queryser = self.get_queryset().filter(category=pk)
        serializer = self.get_serializer(queryser,many=True)
        return Response(serializer.data)


    def get_queryset(self):
        if self.action == 'list':
            queryset = Category.objects.filter(parent=None)
        else:
            queryset = Product.objects.all()
        return queryset
    

    def get_serializer_class(self):
        if self.action == 'list':
            serializer_class = CategorySerializers
        else:
            serializer_class = ProductSerializers
        return serializer_class
    