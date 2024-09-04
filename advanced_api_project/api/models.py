from django.db import models

class Author(models.Model):
     # The Author model stores information about book authors.
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    # The Book model stores details about books, including the title, publication year,
    # and a ForeignKey to the Author model, establishing a one-to-many relationship.
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

