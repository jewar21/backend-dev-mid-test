import argparse
from library_system.models import Book, Member, Library
from library_system.persistence.persistence import load_books_from_json, store_books_to_json

BOOKS_JSON_PATH = "library_system/persistence/books.json"

# Crear biblioteca y cargar libros
library = Library()
books = load_books_from_json(BOOKS_JSON_PATH)
for book in books:
    library.add_book(book)

# Agregar miembros manualmente (TODO: Mejorar luego con persistencia)
member1 = Member(101, "Yisus", "yisus@yisus.com")
member2 = Member(102, "Edwar", "edwar@edwar.com")
library.add_member(member1)
library.add_member(member2)

# Setup del parser
parser = argparse.ArgumentParser(description="Gestor CLI de Biblioteca")
parser.add_argument("--list", action="store_true", help="Listar todos los libros")
parser.add_argument("--lend", type=int, help="Prestar libro (por ID)")
parser.add_argument("--return_book", type=int, help="Devolver libro (por ID)")
parser.add_argument("--member", type=int, help="ID del miembro (requerido para prestar o devolver)")

args = parser.parse_args()

if args.list:
    print("\nEstado actual de los libros:")
    for book in library.books:
        status = "Prestado" if book.is_borrowed else "Disponible"
        print(f"- ID {book.book_id}: {book.title} ({status})")

elif args.lend and args.member:
    book = next((b for b in library.books if b.book_id == args.lend), None)
    if book:
        library.lend_book(book, args.member)
        print(f"✅ Libro '{book.title}' prestado al miembro {args.member}")
    else:
        print(f"❌ Libro con ID {args.lend} no encontrado.")

elif args.return_book and args.member:
    book = next((b for b in library.books if b.book_id == args.return_book), None)
    if book:
        library.receive_book(book, args.member)
        print(f"✅ Libro '{book.title}' devuelto por el miembro {args.member}")
    else:
        print(f"❌ Libro con ID {args.return_book} no encontrado.")

else:
    print("⚠️ No se proporcionó una acción válida. Usa --help para ver opciones.")

# Guardar estado actualizado
store_books_to_json(library.books, BOOKS_JSON_PATH)
