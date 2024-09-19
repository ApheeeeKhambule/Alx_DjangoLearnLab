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
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Check if user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# View for Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# View for Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# View for Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
