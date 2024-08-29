import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print("Author not found")

# List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print("Library not found")

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(librarian.name)
    except Library.DoesNotExist:
        print("Library not found")
    except Librarian.DoesNotExist:
        print("Librarian not found")

# Example usage
if __name__ == "__main__":
    print("Books by Author 'John Doe':")
    get_books_by_author("John Doe")

    print("\nBooks in Library 'Central Library':")
    list_books_in_library("Central Library")

    print("\nLibrarian for Library 'Central Library':")
    get_librarian_for_library("Central Library")
