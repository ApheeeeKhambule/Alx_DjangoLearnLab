from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]

urlpatterns = [
   path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
   path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
   path('register/', views.register, name='register'),
   path('profile/', views.profile, name='profile'),
]

urlpatterns = [
    path('', views.home, name='home'),  # Link the view to the home page
]
