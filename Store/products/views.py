from rest_framework.generics import ListAPIView , RetrieveAPIView
from .serializer_ import ProductSerializers
from .models import Product


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductRetrieveView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = ProductSerializers


    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset