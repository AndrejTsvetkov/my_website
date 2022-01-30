from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('posts/', views.get_posts),
    path('posts/<int:pk>/', views.get_post),
    path('comments/', views.get_comments),
    path('comments/<int:pk>/', views.get_comment),
    path('post_comments/', views.get_post_with_comments),
]
