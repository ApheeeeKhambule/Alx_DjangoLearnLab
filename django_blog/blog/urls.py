
from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)
# blog/urls.py
from django.urls import path
from . import views

from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    # Other URL patterns for your blog app
    
    # URL pattern for creating a new comment
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),

    # URL pattern for updating an existing comment
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),

    # URL pattern for deleting an existing comment
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]



urlpatterns = [
    # Other URL patterns
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
    path('search/', views.search_posts, name='search_posts'),
]


urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

