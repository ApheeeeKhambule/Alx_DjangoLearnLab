from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255, unique=True))

    def __str__(self):
        return self.name
 ["class UserProfile(models.Model):", "Admin", "Member"]
 ["class Meta", "permissions"]
["can_add_book", "can_change_book", "can_delete_book"]

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Library Model
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
