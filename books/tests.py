from django.test import TestCase
from django.urls import reverse

from books.models import Book


# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="A good subtitle",
            author="Tom Davinski",
            isbn="123459842",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.subtitle, "A good subtitle")
        self.assertEqual(self.book.author, "Tom Davinski")
        self.assertEqual(self.book.isbn, "123459842")

    def test_book_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "books/book_list.html")
