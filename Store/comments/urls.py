
from django.urls import path , include
from .views import  CommentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'comment', CommentViewSet, basename='comment')


app_name = 'comments'


urlpatterns = [
    path('v1/',include(router.urls))
]