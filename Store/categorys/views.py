from .serializer_ import CategorySerializers
from .models import Category
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    lookup_field = 'pk'
    http_method_names = ['get']
    search_fields = ['title']
    filter_backends = [SearchFilter]

    def get_queryset(self):
        queryset = Category.objects.filter(parent=None)
        return queryset