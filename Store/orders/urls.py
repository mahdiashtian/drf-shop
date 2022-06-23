from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet


router = DefaultRouter()
router.register(r'user/order/(?P<id>\d+)/manage', OrderViewSet,basename='order')
    

app_name = 'orders'


urlpatterns = [
   path('v1/',include(router.urls))
]