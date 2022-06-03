import imp
from rest_framework.generics import ListAPIView , CreateAPIView
from .serializer_ import CommentٰViewSerializers , CommentٰAddSerializers
from .models import Comment
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from Store.permissions import IsStaffOrReadOnly

class CommentView(ListAPIView):
    serializer_class = CommentٰViewSerializers
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated,]


    def get_queryset(self):
        query_string = self.kwargs
        pk = query_string['pk']
        lockup = (Q(product__id=pk))
        queryset = Comment.objects.filter(lockup)     
        return queryset


class CommentAdd(CreateAPIView):
    serializer_class = CommentٰAddSerializers
    permission_classes = [IsAuthenticated]

