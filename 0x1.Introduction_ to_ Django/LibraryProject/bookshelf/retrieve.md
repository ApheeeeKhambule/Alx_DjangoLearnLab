# Retrieve Operation for Book Model

## Command

```python
from bookshelf.models import Book

# Retrieve the Book instance
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
