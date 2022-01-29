# from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blog.models import Post, Comment
from django.utils import timezone


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    date_posted = serializers.DateTimeField(default=timezone.now)
    author = serializers.CharField(source='author.username')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
