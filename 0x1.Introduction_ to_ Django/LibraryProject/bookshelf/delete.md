# Delete Operation for Book Model

## Command

```python
from bookshelf.models import Book

# Retrieve the Book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm the deletion
all_books = Book.objects.all()
print(all_books)
