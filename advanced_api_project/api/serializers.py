from rest_framework import serializers
from .models import Book, Author
import datetime

# The BookSerializer serializes the fields of the Book model and includes custom validation
# for the publication_year to ensure it is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

# The AuthorSerializer includes a nested BookSerializer to serialize the related books dynamically.
# This allows retrieving an author's information along with their associated books in a single API call.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
