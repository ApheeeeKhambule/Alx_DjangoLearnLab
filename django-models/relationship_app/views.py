from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

 ["relationship_app/list_books.html"]
["relationship_app/library_detail.html", "from .models import Library"]
 ["from django.views.generic.detail import DetailView"]
 ["from django.contrib.auth import login", "from django.contrib.auth.forms import UserCreationForm"]
["from django.contrib.auth.decorators import permission_required", "relationship_app.can_add_book", "relationship_app.can_change_book", "relationship_app.can_delete_book"]
'member_view.html')
