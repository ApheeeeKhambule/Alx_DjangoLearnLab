from django.shortcuts import render

# Create a view that renders the home.html template
def home(request):
    return render(request, 'blog/home.html')

