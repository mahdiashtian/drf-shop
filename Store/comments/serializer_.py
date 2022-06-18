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
    
    confirmation = serializers.BooleanField(default=True,read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
