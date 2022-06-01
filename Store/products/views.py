from .serializer_ import ProductSerializers
from .models import Product
from rest_framework.generics import ListAPIView


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers