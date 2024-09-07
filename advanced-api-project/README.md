# Advanced API Project with Django REST Framework

This project demonstrates CRUD operations for a `Book` model using Django REST Framework's generic views and custom permissions.

## API Endpoints

- **List all books**: `GET /api/books/`
- **Retrieve a book by ID**: `GET /api/books/<int:pk>/`
- **Create a new book**: `POST /api/books/` (Authenticated users only)
- **Update a book**: `PUT /api/books/<int:pk>/` (Authenticated users only)
- **Delete a book**: `DELETE /api/books/<int:pk>/` (Authenticated users only)

## Permissions

- Unauthenticated users can view books.
- Only authenticated users can create, update, and delete books.
