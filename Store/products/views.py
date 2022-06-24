from .serializers_ import ProductSerializers
from .models import Product
from rest_framework import viewsets
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter , OrderingFilter
from .mixins import AddView


class ProductViewSet(AddView,viewsets.ReadOnlyModelViewSet):
    lookup_field = 'pk'
    search_fields = ['title','category__title']
    ordering_fields = ['price']
    serializer_class = ProductSerializers
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset