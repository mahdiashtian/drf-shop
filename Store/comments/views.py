import imp
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView,ListAPIView
from .serializer_ import CommentSerializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Comment
from rest_framework.permissions import IsAuthenticated


class CommentListView(ListAPIView):
    serializer_class = CommentSerializers
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        query_string = self.kwargs
        pk = query_string['pk']
        queryset = Comment.objects.filter(product__id=pk)     
        return queryset