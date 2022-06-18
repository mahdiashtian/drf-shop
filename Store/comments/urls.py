
from django.urls import path
from .views import CommentView,CommentAdd,CommentDelete


app_name = 'comments'


urlpatterns = [
    path('v1/product/<int:pk>/comment-view/', CommentView.as_view(),name='comment-list'),
    path('v1/product/<int:pk>/comment-add/', CommentAdd.as_view(),name='comment-add'),
    path('v1/product/<int:pk>/comment-delete/<int:id>/', CommentDelete.as_view(),name='comment-delete'),
]