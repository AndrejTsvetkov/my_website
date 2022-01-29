from ..models import Post
from django import template

register = template.Library()


@register.simple_tag()
def get_recent_posts(num=3):
    return Post.objects.all().order_by('-date_posted')[:num]
