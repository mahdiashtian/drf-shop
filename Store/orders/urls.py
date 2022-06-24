from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet , OrderDetailViewSet


router = DefaultRouter()
router.register(r'user/order', OrderViewSet,basename='order-vi')
router.register(r'user/order/(?P<id>\d+)', OrderDetailViewSet,basename='order-dt')
    

app_name = 'orders'


urlpatterns = [
   path('v1/',include(router.urls))
]