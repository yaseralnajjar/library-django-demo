import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Book
from .serializers import BookSerializer

User = get_user_model()


class BookListCreateAPIViewTestCase(APITestCase):
    url = reverse('books:list')

    def setUp(self):
        self.username = 'john'
        self.email = 'john@snow.com'
        self.password = 'you_know_nothing'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_book(self):
        response = self.client.post(self.url, {'name': 'Awesome Book',
                                               'isbn': '978-3-16-148410-0',
                                               'publish_date': '2020-01-01',
                                               'author': self.user.id})
        self.assertEqual(201, response.status_code)

    def test_bad_isbn(self):
        response = self.client.post(self.url, {'name': 'Awesome Book',
                                               'isbn': '123456',
                                               'publish_date': '2020-01-01',
                                               'author': self.user.id})
        self.assertEqual(400, response.status_code)

    def test_user_books(self):
        '''
        Test to verify author books list
        '''
        Book.objects.create(name='Awesome Book', isbn='978-3-16-148410-0',
                            publish_date='2020-01-01', author=self.user)
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == Book.objects.count())


class BookDetailAPIViewTestCase(APITestCase):

    def setUp(self):
        self.username = 'john'
        self.email = 'john@snow.com'
        self.password = 'you_know_nothing'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.book = Book.objects.create(name='Awesome Book', isbn='978-3-16-148410-0',
                                        publish_date='2020-01-01', author=self.user)
        self.url = reverse('books:detail', kwargs={'pk': self.book.pk})
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_book_object_bundle(self):
        '''
        Test to verify book object bundle
        '''
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        book_serializer_data = BookSerializer(instance=self.book).data
        response_data = json.loads(response.content)
        self.assertEqual(book_serializer_data, response_data)

    def test_book_object_update_authorization(self):
        '''
            Test to verify that put call with different user token
        '''
        new_user = User.objects.create_user('newuser', 'new@user.com', 'newpass')
        new_token = Token.objects.create(user=new_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)

        # HTTP PUT
        response = self.client.put(self.url, {'name': 'New Name',
                                              'isbn': self.book.isbn,
                                              'publish_date': self.book.publish_date,
                                              'author': self.user.id})
        self.assertEqual(403, response.status_code)

        # HTTP PATCH
        response = self.client.patch(self.url, {'name': 'Hacked by new user'})
        self.assertEqual(403, response.status_code)

    def test_book_object_update(self):
        response = self.client.put(self.url, {'name': 'New Name',
                                              'isbn': self.book.isbn,
                                              'publish_date': self.book.publish_date,
                                              'author': self.user.id})
        response_data = json.loads(response.content)
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(response_data.get('name'), book.name)

    def test_book_object_partial_update(self):
        response = self.client.patch(self.url, {'name': 'New Name'})
        response_data = json.loads(response.content)
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(response_data.get('name'), book.name)

    def test_book_object_delete_authorization(self):
        '''
            Test to verify that put call with different user token
        '''
        new_user = User.objects.create_user('newuser', 'new@user.com', 'newpass')
        new_token = Token.objects.create(user=new_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)
        response = self.client.delete(self.url)
        self.assertEqual(403, response.status_code)

    def test_book_object_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)
