from django.db import models

# The Author model represents an author with a name.
# One author can have many books (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# The Book model represents a book, which includes a title, publication year,
# and a foreign key to the Author model, establishing a one-to-many relationship.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
