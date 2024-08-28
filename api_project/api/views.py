
# api/views.py
from rest_framework.generics.ListAPIView  # Correct import from DRF generics
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):  # Correctly extending ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer
