import json
from library_system.models import Book

def load_books_from_json(ruta: str) -> list[Book]:
    """Carga libros desde un archivo JSON y retorna una lista de objetos Book."""
    with open(ruta, "r", encoding="utf-8") as f:
        data = json.load(f)

    books = []
    for item in data["books"]:
        book = Book(
            book_id=item["book_id"],
            title=item["title"],
            author=item["author"],
            isbn=item["isbn"]
        )
        book.is_borrowed = item.get("is_borrowed", False)
        books.append(book)

    return books

def store_books_to_json(libros: list[Book], ruta: str) -> None:
    """Guarda una lista de objetos Book en formato JSON."""
    data = {
        "books": [
            {
                "book_id": b.book_id,
                "title": b.title,
                "author": b.author,
                "isbn": b.isbn,
                "is_borrowed": b.is_borrowed
            }
            for b in libros
        ]
    }
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
