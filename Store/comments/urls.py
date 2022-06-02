from django.urls import path
from .views import CommentListView


app_name = 'comments'


urlpatterns = [
    path('product/comment-view/<int:pk>', CommentListView.as_view(),name='Colist'),
]