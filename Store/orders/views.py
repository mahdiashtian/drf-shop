from rest_framework import viewsets
from orders.models import Order , OrderDetail
from .serializers_ import OrderSerializer , OrderDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from django.db.models import Q
from rest_framework import mixins


class ServiceUnavailable(APIException):
    status_code = 409
    default_detail = 'این سبد خرید برای شما نیست'


class OrderViewSet(mixins.ListModelMixin,
                viewsets.GenericViewSet):
    lookup_field = 'pk'
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            queryset = Order.objects.filter(user=user)
            return queryset


class OrderDetailViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        pk = self.kwargs['id']
        if self.request.user.is_authenticated:
            user = self.request.user
            lookup = (Q(order__user=user) & Q(order__id=pk))
            queryset = OrderDetail.objects.filter(lookup)
            if queryset:
                return queryset
            else:
                raise ServiceUnavailable()


    def get_serializer_class(self):
        if self.action == 'update':
            serializer_class = OrderDetailSerializer
            serializer_class.Meta.fields = ('count','product_title','price','url')
        else:
            serializer_class = OrderDetailSerializer
            serializer_class.Meta.fields = ['id','product_title','product','price','order','count','url']
        return serializer_class