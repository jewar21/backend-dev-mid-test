import unittest
from library_system.models import Book, Member, Library

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        # Crear objetos para prueba
        self.library = Library()
        self.book = Book(1, "1984", "George Orwell", "9780451524935")
        self.member = Member(101, "Yisus", "yisus@example.com")
        self.library.add_book(self.book)
        self.library.add_member(self.member)

    def test_borrow_book(self):
        self.library.lend_book(self.book, self.member.member_id)
        self.assertTrue(self.book.is_borrowed)
        self.assertIn(self.book, self.member.borrowed_books)

    def test_return_book(self):
        self.library.lend_book(self.book, self.member.member_id)
        self.library.receive_book(self.book, self.member.member_id)
        self.assertFalse(self.book.is_borrowed)
        self.assertNotIn(self.book, self.member.borrowed_books)

    def test_prevent_double_borrow(self):
        self.library.lend_book(self.book, self.member.member_id)
        member2 = Member(102, "Otro", "otro@example.com")
        self.library.add_member(member2)
        self.library.lend_book(self.book, member2.member_id)
        self.assertNotIn(self.book, member2.borrowed_books)

    def test_nonexistent_member(self):
        self.library.lend_book(self.book, 999)
        self.assertFalse(self.book.is_borrowed)

    def test_nonexistent_book(self):
        fake_book = Book(99, "Falso", "Desconocido", "0000000000")
        self.library.lend_book(fake_book, self.member.member_id)
        self.assertNotIn(fake_book, self.member.borrowed_books)

if __name__ == "__main__":
    unittest.main()
