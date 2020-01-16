from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_admin', 'is_active', 'is_staff']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'title', 'content', 'public', 'user']
