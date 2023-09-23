class Book():
    def __init__(self, id: int, name: str, author: str):
        self.id = id
        self.name = name
        self.author = author

class BookRepository:
    def __init__(self, books: list[Book]):
        self._books = books
        if not books:
            self._books = []

    def get_book_by_id(self, book_id: int) -> Book:
        book = [*filter(lambda x: x.id == book_id, self._books)][0]
        return book

    def get_book_all(self) -> list[Book]:
        return self._books


class BookService:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    @property
    def book_repository(self):
        return self._book_repository

    def get_book_by_id(self, book_id: int) -> Book:
        return self._book_repository.get_book_by_id(book_id)

    def get_book_all(self) -> list[Book]:
        return self._book_repository.get_book_all()
