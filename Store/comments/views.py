from rest_framework.generics import (
    ListAPIView , 
    CreateAPIView , 
    RetrieveDestroyAPIView )

from .serializer_ import (
    CommentٰViewSerializers ,
    CommentٰAddSerializers , 
    CommentAddReplySerializers,
    CommentDeleteReplySerializers,)

from .models import Comment
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from Store.permissions import IsStaffOrReadOnly , Isauthor

class CommentView(ListAPIView):
    serializer_class = CommentٰViewSerializers
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        query_string = self.kwargs
        pk = query_string['pk']
        lockup = (Q(product__id=pk) &  Q(is_reply=False))
        queryset = Comment.objects.filter(lockup)
        return queryset


class CommentAdd(CreateAPIView):
    serializer_class = CommentٰAddSerializers
    permission_classes = [IsAuthenticated]

    
class CommentAddReply(CreateAPIView):
    serializer_class = CommentAddReplySerializers
    permission_classes = [IsAuthenticated]


class CommentDelete(RetrieveDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CommentDeleteReplySerializers
    permission_classes = [IsAuthenticated,Isauthor]


    def get_queryset(self):
        query_string = self.kwargs
        pk = query_string['pk']
        queryset = Comment.objects.filter(id=pk)
        return queryset