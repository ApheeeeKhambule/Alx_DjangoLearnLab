from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
     # The BookSerializer serializes the Book model, including all fields.
    # It also includes a custom validation to ensure the publication year is valid.
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        # Ensure the publication year is not in the future.
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
     # The AuthorSerializer serializes the Author model, including the name field and a nested
    # BookSerializer for serializing related books.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
