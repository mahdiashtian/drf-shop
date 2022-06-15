from django.urls import path , include
from .views import CategoryViewSet 
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet,basename='category')


app_name = 'categorys'


urlpatterns = [
    path('v1/',include(router.urls))
]