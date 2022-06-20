
from rest_framework import generics , viewsets
from .models import Comment
from .serializer_ import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from permissions.permissions import IsAuthor
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    filterset_fields = ['product']
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = Comment.objects.filter(reply=None)
        return queryset


    def get_permissions_calsses(self):
        if self.action in ['get','post']:
            return [IsAuthenticated]
        return [IsAuthenticated,IsAuthor]