from django.urls import path , include
from .views import CategoryViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')


app_name = 'categorys'


urlpatterns = [
    path('v1/',include(router.urls))
]