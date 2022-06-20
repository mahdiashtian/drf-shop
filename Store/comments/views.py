
from rest_framework import generics
from .models import Comment
from .serializer_ import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from permissions.permissions import IsAuthor
from django.db.models import Q


class CommentView(generics.ListAPIView):
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):
        query_string = self.kwargs
        pk = query_string['pk']
        lockup = (Q(product__id=pk) &  Q(reply=None))
        queryset = Comment.objects.filter(lockup)
        return queryset


class CommentAdd(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    

class CommentDelete(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,IsAuthor]


    def get_queryset(self):
        query_string = self.kwargs
        pk = query_string['pk']
        id_ = query_string['id']
        queryset = Comment.objects.filter(id=id_)
        return queryset