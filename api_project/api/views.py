
# api/views.py
from rest_framework import viewsets  # Import viewsets from DRF
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):  # Extend ModelViewSet for CRUD operations
    queryset = Book.objects.all()
    serializer_class = BookSerializer
