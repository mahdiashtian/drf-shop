from dataclasses import fields
from email.policy import default
from pyexpat import model
from click import edit
from numpy import source
from rest_framework import serializers
from sqlalchemy import null
from .models import Comment
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin


User = get_user_model()


class CommentSerializer(DynamicFieldsMixin,serializers.ModelSerializer):

    @staticmethod
    def get_reply_(obj):
        return CommentSerializer(obj.comment_reply.all(), many=True).data


    def get_user_(self,obj):
        user = obj.user
        return {
            'id':user.id,
            'name':f"{user.first_name}  {user.last_name}",
            'username':f"{user.username}"
        }


    user_ = serializers.SerializerMethodField('get_user_')

    reply_ = serializers.SerializerMethodField()

    class Meta:
        model = Comment

        fields = [
            'id',
            'user_',
            'reply_',
            'user',
            'product',
            'reply',
            'date_time_added',
            'confirmation',
            'main_message',
        ]

        read_only_fields = [
            'confirmation',
            'reply_',
            'user_',
            ]

        extra_kwargs = {
            'user':{'write_only':True},
            'product':{'write_only':True},
            'reply':{'write_only':True},
        }


    def validate_user(self,value):
        if self.context['request'].user != value:
            raise serializers.ValidationError("شما حق دسترسی ندارید")
        return value


    def validate(self,data):
        if data['product'] and data['reply']:
            raise serializers.ValidationError("مقادیر ارسالی نامعتبر می با شد") 
        return data
