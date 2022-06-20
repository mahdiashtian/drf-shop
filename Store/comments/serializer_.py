from dataclasses import fields
from email.policy import default
from pyexpat import model
from click import edit
from numpy import source
from rest_framework import serializers
from sqlalchemy import null
from .models import Comment
from django.contrib.auth import get_user_model


User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    
    def get_user(self,obj):
        user = obj.user
        result = {
                'id':user.id,
                'username':user.username,
                'name':user.first_name+' '+user.last_name
                }
        
        return result


    def get_reply(self,obj):
        reply = obj.comment_reply.all()
        result = [
            [
                {
                "user":{                 
                    'id':i.user.id,
                    'username':i.user.username,
                    'name':i.user.first_name+' '+i.user.last_name},
                
                "reply":{
                    'id':i.id,
                    'date_time_added':i.date_time_added,
                    'confirmation':i.confirmation,
                    'main_message':i.main_message,
                },
                }
            ]
        for i in reply]

        return result
    

    User = serializers.SerializerMethodField('get_user')

    Reply = serializers.SerializerMethodField('get_reply')

    class Meta:
        model = Comment

        fields = [
            'id',
            'User',
            'Reply',
            'user',
            'product',
            'reply',
            'date_time_added',
            'confirmation',
            'main_message',
        ]

        read_only_fields = [
            'confirmation',
            'User',
            'Reply',
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


    def validate_reply(self, value):
        if value and value.reply:
            raise serializers.ValidationError("مقادیر ارسالی نامعتبر می با شد") 


    def validate(self,data):
        if data['product'] and data['reply']:
            raise serializers.ValidationError("مقادیر ارسالی نامعتبر می با شد") 
        return data
