from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
   path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
   path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
   path('register/', views.register, name='register'),
   path('profile/', views.profile, name='profile'),
]

urlpatterns = [
    path('', views.home, name='home'),  # Link the view to the home page
]
