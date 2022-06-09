from dataclasses import fields
from pyexpat import model
from numpy import source
from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name')


class CommentReplySerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)

    class Meta:
        model = Comment
        exclude = ('reply','product')


class CommentٰViewSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    reply = CommentReplySerializers(many=True,source='get_reply',read_only=True)

    class Meta:
        model = Comment
        fields = ('id','user','date_time_added','date_time_edit','confirmation','main_message','reply')


class CommentٰAddSerializers(serializers.ModelSerializer):    
    is_reply = serializers.BooleanField(default=False,read_only=True)

    class Meta:
        model = Comment
        exclude = ('confirmation','reply')


class CommentAddReplySerializers(serializers.ModelSerializer):
    reply = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.filter(is_reply=False))
    is_reply = serializers.BooleanField(default=True,read_only=True)

    class Meta:
        model = Comment
        exclude = ('product','confirmation')


class CommentDeleteReplySerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

