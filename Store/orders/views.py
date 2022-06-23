from cgitb import lookup
from rest_framework import viewsets
from orders.models import Order , OrderDetail
from .serializers_ import OrderSerializer , OrderDetailSerializer
from permissions.permissions import IsAuthor
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from django.db.models import Q


class ServiceUnavailable(APIException):
    status_code = 409
    default_detail = 'این سبد خرید برای شما نیست و یا پرداخت شده است'


class OrderViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk'


    def get_queryset(self):
        pk = self.kwargs['id']
        if self.request.user.is_authenticated:
            user = self.request.user
            lookup = (Q(order__user=user) & Q(order__id=pk) & Q(order__is_paid=False))
            queryset = OrderDetail.objects.filter(lookup)
            if queryset:
                return queryset
            else:
                raise ServiceUnavailable()


    def get_serializer_class(self):
        if self.action == 'update':
            serializer_class = OrderDetailSerializer
            serializer_class.Meta.fields = ('count','product_title','price')
        else:
            serializer_class = OrderDetailSerializer
            serializer_class.Meta.fields = ['id','product_title','product','price','order','count']
        return serializer_class
    

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]