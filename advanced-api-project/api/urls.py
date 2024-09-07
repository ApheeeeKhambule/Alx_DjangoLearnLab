from django.urls import path
from .views import BookCreateView, BookUpdateView, BookDeleteView, BookDetailView, BookListView

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Retrieve details of a specific book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Update a specific book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # Delete a specific book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]

