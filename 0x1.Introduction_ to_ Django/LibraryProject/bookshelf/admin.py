from django.contrib import admin
from .models import Book

# Customizing the admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    list_filter = ('author', 'publication_year')  # Fields to filter by in the admin
    search_fields = ('title', 'author')  # Fields to add search functionality

# Register the Book model to make it available in the admin
admin.site.register(Book)
