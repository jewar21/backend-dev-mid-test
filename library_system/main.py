from models import Book, Member, Library

# Crear instancia de Library
library = Library()

# Agregar libros
book1 = Book(1, "1984", "George Orwell", "9780451524935")
book2 = Book(2, "Clean Code", "Robert C. Martin", "9780132350884")
library.add_book(book1)
library.add_book(book2)

# Agregar miembros
member1 = Member(101, "Yisus", "yisus@yisus.com")
member2 = Member(102, "Edwar", "edwar@edwar.com")
library.add_member(member1)
library.add_member(member2)

# Mostrar estado inicial
print("\n Estado inicial de los libros:")
for book in library.books:
    status = "Prestado" if book.is_borrowed else "Disponible"
    print(f"- {book.title} ({status})")
    
#TODO: Crear los demás casos, préstamo, devolución... etc
