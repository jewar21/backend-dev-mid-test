from library_system.models import Member, Library
from library_system.persistence.persistence import load_books_from_json, store_books_to_json

BOOKS_JSON_PATH = "library_system/persistence/books.json"

# Crear instancia de Library
library = Library()

# Cargar libros desde JSON
books =load_books_from_json(BOOKS_JSON_PATH)
for book in books:
    library.add_book(book)


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
print("\n Prestando libro a Yisus...")
library.lend_book(library.books[0], member1.member_id)

# Mostrar estado actualizado
print("\n Estado de los libros después del préstamo:")
for book in library.books:
    status = "Prestado" if book.is_borrowed else "Disponible"
    print(f"- {book.title} ({status})")

# Simular devolución
print("\n Devolviendo libro de Yisus...")
library.receive_book(library.books[0], member1.member_id)

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
    
store_books_to_json(library.books, BOOKS_JSON_PATH)