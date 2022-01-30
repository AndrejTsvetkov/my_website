# from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blog.models import Post, Comment
from django.utils import timezone


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class SupCommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='name.username')

    class Meta:
        model = Comment
        fields = ['body', 'created_on', 'author']


class PostCommentSerializer(serializers.ModelSerializer):
    comments = SupCommentSerializer(many=True)
    author = serializers.CharField(source='author.username')

    class Meta:
        model = Post
        fields = ['title', 'content', 'date_posted', 'author', 'comments']
