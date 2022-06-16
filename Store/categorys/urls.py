from django.urls import path , include
from .views import CategoryListView, CategoryRetrieveView


app_name = 'categorys'


urlpatterns = [
    path('v1/category/', CategoryListView.as_view(),name='category-list'),
    path('v1/category/<pk>/', CategoryRetrieveView.as_view(),name='category-detail')
]