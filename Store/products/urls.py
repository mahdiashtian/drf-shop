from django.urls import path
from .views import ProductListView,ProductRetrieveView


app_name = 'products'


urlpatterns = [
    path('product', ProductListView.as_view(),name='Prlist'),
    path('product/<int:pk>', ProductRetrieveView.as_view(),name='Prretrieve'),
]