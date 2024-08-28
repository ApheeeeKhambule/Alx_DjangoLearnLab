from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author (replace 'author_name' with the actual name)
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = author.books.all()
print(f"Books by {author_name}: {books_by_author}")

# List all books in a library (replace 'library_name' with the actual name)
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}: {books_in_library}")

# Retrieve the librarian for a library (replace 'library_name' with the actual name)
library_name = "Central Library"
library = Library.objects.get(name=library_name)
librarian = library.librarian
print(f"Librarian for {library_name}: {librarian}")
