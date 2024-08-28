# Admin Setup for Book Model

## Steps to Integrate the Book Model with Django Admin

1. **Create `admin.py` File**
   - Navigate to the `bookshelf` app directory.
   - Create or open the `admin.py` file.

2. **Register the Book Model**
   - Add the following code to `admin.py`:

     ```python
     from django.contrib import admin
     from .models import Book

     class BookAdmin(admin.ModelAdmin):
         list_display = ('title', 'author', 'publication_year')
         list_filter = ('author', 'publication_year')
         search_fields = ('title', 'author')

     admin.site.register(Book, BookAdmin)
     ```

3. **Customize the Admin Interface**
   - `list_display`: Configures fields to be shown in the list view.
   - `list_filter`: Adds filter options for `author` and `publication_year`.
   - `search_fields`: Enables search functionality for `title` and `author`.

4. **Save and Test**
   - Save the changes to `admin.py`.
   - Run the Django development server.
   - Access the admin interface to ensure the Book model is properly integrated and customizable.

## Expected Outcome
- The `Book` model should be visible in the Django admin interface.
- The list view should display the `title`, `author`, and `publication_year`.
- Filters and search functionality should be available for managing book entries.
