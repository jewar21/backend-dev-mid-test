class Book:
    def __init__(self, book_id: int, title: str, author: str, isbn: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self) -> None:
        """Marca el libro como prestado."""
        self.is_borrowed = True

    def return_book(self) -> None:
        self.is_borrowed = False


class Member:
    def __init__(self, member_id: int, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book) -> None:
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.members: list[Member] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def add_member(self, member: Member) -> None:
        self.members.append(member)

    def lend_book(self, book: Book, member_id: int) -> None:
        member = self._find_member_by_id(member_id)
        if member and book in self.books and not book.is_borrowed:
            member.borrow_book(book)

    def receive_book(self, book: Book, member_id: int) -> None:
        member = self._find_member_by_id(member_id)
        if member and book in member.borrowed_books:
            member.return_book(book)

    # Función auxiliar "privada"
    def _find_member_by_id(self, member_id: int) -> Member | None:
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None
