
# api/views.py
from rest_framework.generics import ListAPIView  # Correct import
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):  # Correct usage of ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer
