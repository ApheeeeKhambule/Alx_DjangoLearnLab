# relationship_app/query_samples.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Example queries
if __name__ == "__main__":
    print("Books by J.K. Rowling:")
    for book in query_books_by_author("J.K. Rowling"):
        print(book.title)

    print("\nBooks in Central Library:")
    for book in list_books_in_library("Central Library"):
        print(book.title)

    print("\nLibrarian for Central Library:")
    librarian = get_librarian_for_library("Central Library")
    print(librarian.name)
