from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create a view that renders the home.html template
def home(request):
    return render(request, 'blog/home.html')
