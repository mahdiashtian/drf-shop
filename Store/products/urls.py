from django.urls import path , include
from .views import ProductViewSet 
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'product', ProductViewSet,basename='product')


app_name = 'products'


urlpatterns = [
    path('v1/',include(router.urls))
]