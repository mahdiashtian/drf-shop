from django.urls import path
from .views import CommentView,CommentAdd,CommentAddReply,CommentDelete


app_name = 'comments'


urlpatterns = [
    path('v1/product/comment-view/<int:pk>', CommentView.as_view(),name='Colist'),
    path('v1/product/comment-add/<int:pk>', CommentAdd.as_view(),name='Coadd'),
    path('v1/product/comment-reply/<int:pk>', CommentAddReply.as_view(),name='Coaddreply'),
    path('v1/product/comment-delete/<int:pk>', CommentDelete.as_view(),name='Codelete'),
]