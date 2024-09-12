from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Link the view to the home page
]
