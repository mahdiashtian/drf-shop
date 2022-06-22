from rest_framework import viewsets
from .models import Comment
from .serializers_ import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from permissions.permissions import IsAuthor
from django.db.models import Q


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs['id']
        query = (Q(product_id=pk) & Q(reply=None))
        return Comment.objects.filter(query)


    def get_permissions(self):
        if self.action in ['get']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated,IsAuthor]
        return [permission() for permission in permission_classes]