# Update Operation for Book Model

## Command

```python
from bookshelf.models import Book

# Retrieve the Book instance
book = Book.objects.get(title="1984")

# Update the book's title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book.title)
