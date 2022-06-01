from django.contrib import admin
from django.urls import path
from Store import settings
from .views import ProductListView


app_name = 'products'


urlpatterns = [
    path('product', ProductListView.as_view(),name='Prlist'),
]