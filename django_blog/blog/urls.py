
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import add_comment, edit_comment, delete_comment

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comments/<int:pk>/edit/', edit_comment, name='edit-comment'),
    path('comments/<int:pk>/delete/', delete_comment, name='delete-comment'),
]


from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView
)

urlpatterns = [
    # URL for listing all posts
    path('posts/', PostListView.as_view(), name='post-list'),

    # URL for creating a new post
    path('posts/new/', PostCreateView.as_view(), name='post-create'),

    # URL for viewing details of a specific post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # URL for updating/editing a specific post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),

    # URL for deleting a specific post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
