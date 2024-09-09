# blog/urls.py
from django.urls import path
from accounts import views as account_views

urlpatterns = [
    path('register/', account_views.register, name='register'),
    path('login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view, name='logout'),
    path('profile/', account_views.profile, name='profile'),
]
