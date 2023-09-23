import unittest
from unittest.mock import Mock

from book_service import BookService


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book_service = BookService(Mock())
        self.book_id = 7

    def test_get_book_by_id(self):
        self.book_service.get_book_by_id(self.book_id)
        self.book_service.book_repository.get_book_by_id.assert_called_with(self.book_id)

    def test_get_book_all(self):
        self.book_service.get_book_all()
        self.book_service.book_repository.get_book_all.assert_called_once()
