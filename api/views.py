from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, PostCommentSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api',
        'GET /api/posts',
        'GET /api/posts/:id',
        'GET /api/comments',
        'GET /api/comments/:id',
        'GET /api/post_comments/'
    ]
    return Response(routes)


@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_post(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_comments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_post_with_comments(request):
    posts = Post.objects.all()
    serializer = PostCommentSerializer(posts, many=True)
    return Response(serializer.data)
