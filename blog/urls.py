from django.urls import path
from .views import (
    MainView,
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    CommentCreateView,
    CommentDeleteView,
    PostLikeToggle,
    PostDislikeToggleView,
    RegisterView,
)

urlpatterns = [
    path('', MainView.as_view(), name='main'),  
    path('register/', RegisterView.as_view(), name='register'),  
    path('posts/', PostListView.as_view(), name='post_list'),  
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  
    path('post/new/', PostCreateView.as_view(), name='post_create'),  
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),  
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  
    path('post/<int:pk>/like/', PostLikeToggle.as_view(), name='post_like_toggle'),  
    path('post/<int:pk>/dislike/', PostDislikeToggleView.as_view(), name='post_dislike_toggle'),  
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),  
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),  
]
