from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),    
]
["views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]
 ["add_book/", "edit_book/", "delete_book"]
