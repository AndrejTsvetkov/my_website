from ..models import Post
from django import template

register = template.Library()


@register.simple_tag()
def get_recent_posts(num=3):
    return Post.objects.all().order_by('-date_posted')[:num]


@register.simple_tag()
def get_popular_posts(num=3):
    queryset = Post.objects.all()
    queryset = sorted(queryset, key=lambda i: i.comments.count(), reverse=True)
    return queryset[:num]
