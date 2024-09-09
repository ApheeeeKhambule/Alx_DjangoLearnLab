from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'
