from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author
from .serializers import BookSerializer

class BookAPITestCase(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.author = Author.objects.create(name="Author Name")
        cls.book = Book.objects.create(
            title="Book Title",
            publication_year=2022,
            author=cls.author
        )
    
    def setUp(self):
        # Log in the user for authentication
        self.client.login(username='testuser', password='testpassword')

    def test_create_book(self):
        url = '/api/books/'
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_update_book(self):
        url = f'/api/books/{self.book.id}/'
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_delete_book(self):
        url = f'/api/books/{self.book.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_list_books(self):
        url = '/api/books/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data[0])

    def test_search_books(self):
        url = '/api/books/?search=Book Title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books(self):
        url = '/api/books/?title=Book Title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering_books(self):
        url = '/api/books/?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book Title')  # Ensure ordering is correct

    def test_permissions(self):
        # Testing without login
        self.client.logout()  # Ensure user is logged out
        url = '/api/books/'
        response = self.client.post(url, {'title': 'Another Book', 'publication_year': 2023, 'author': self.author.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Expecting forbidden access
