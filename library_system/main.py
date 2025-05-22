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

# Simular préstamo
print("\n Prestando '1984' a Alice...")
library.lend_book(book1, 101)

# Mostrar estado actualizado
print("\n Estado de los libros después del préstamo:")
for book in library.books:
    status = "Prestado" if book.is_borrowed else "Disponible"
    print(f"- {book.title} ({status})")

# Simular devolución
print("\n Devolviendo '1984' de Alice...")
library.receive_book(book1, 101)

# Estado final
print("\n Estado final de los libros:")
for book in library.books:
    status = "Prestado" if book.is_borrowed else "Disponible"
    print(f"- {book.title} ({status})")

# Ver qué libros tiene cada miembro
print("\n Libros prestados por miembros:")
for member in library.members:
    titles = [book.title for book in member.borrowed_books]
    print(f"- {member.name}: {titles if titles else 'Ninguno'}")