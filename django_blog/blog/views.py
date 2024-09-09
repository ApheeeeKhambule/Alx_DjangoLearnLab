from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'

@login_required
def profile(request):
    if request.method == 'POST':
        # Handle profile update
        request.user.email = request.POST.get('email', request.user.email)
        request.user.save()
    return render(request, 'blog/profile.html', {'user': request.user})