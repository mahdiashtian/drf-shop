from .serializer_ import ProductSerializers
from .models import Product
from rest_framework import viewsets
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter , OrderingFilter
from .mixins import AddView


class ProductViewSet(AddView,viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    filterset_class = ProductFilter
    search_fields = ['title','category__title']
    ordering_fields = ['price']
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset