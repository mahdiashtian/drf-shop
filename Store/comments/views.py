from rest_framework import viewsets
from .models import Comment
from .serializers_ import CommentSerializer
from rest_framework.permissions import IsAuthenticated


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]


    def perform_update(self, serializer):
        serializer.save(confirmation=False)


    def get_queryset(self):
        if self.action == 'list':
            pk = self.kwargs['id']
            queryset = Comment.objects.filter(product=pk,reply=None)
        else:
            id_ = self.kwargs['pk']
            user = self.request.user
            queryset = Comment.objects.filter(id=id_,user=user)
        return queryset


    def get_serializer_class(self):
        serializer_class = CommentSerializer
        if self.action == 'update':
            serializer_class.Meta.fields = ['main_message','user_','reply_']
        else:
            serializer_class.Meta.fields = [
            'id',
            'user',
            'product',
            'reply',
            'date_time_added',
            'confirmation',
            'main_message',
            'user_',
            'reply_',
        ]
        return serializer_class