from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Demo Book",
            author="Author A",
            isbn="1234567890123",
            published_date="2020-01-01"
        )
        self.create_url = reverse('api:books-list')
        self.detail_url = reverse('api:books-detail', args=[self.book.id])

    def test_list_books(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_create_book(self):
        data = {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "isbn": "9780132350884",
            "published_date": "2008-08-01"
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], self.book.title)

    def test_update_book(self):
        updated_data = {
            "title": "Updated Title",
            "author": self.book.author,
            "isbn": self.book.isbn,
            "published_date": self.book.published_date
        }
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

class HealthViewTest(APITestCase):
    def test_health_check_returns_ok(self):
        response = self.client.get(reverse('api:health'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')
