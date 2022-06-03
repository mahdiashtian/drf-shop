from django.urls import path
from .views import CommentView,CommentAdd


app_name = 'comments'


urlpatterns = [
    path('product/comment-view/<int:pk>', CommentView.as_view(),name='Colist'),
    path('product/comment-add/<int:pk>', CommentAdd.as_view(),name='Coadd'),

]