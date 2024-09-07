# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# BookListView:
# Handles listing all books and creating new books.
# Only authenticated users can create books, while everyone can view them.
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Customize the book creation process (if needed).
        serializer.save()

# BookDetailView:
# Handles retrieving, updating, and deleting a single book by ID.
# Only authenticated users can update or delete books, while everyone can view them.
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
