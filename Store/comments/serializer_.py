from pyexpat import model
from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','last_login','first_name')


class CommentٰViewSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    class Meta:
        model = Comment
        fields = '__all__'


class CommentٰAddSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('confirmation',)


