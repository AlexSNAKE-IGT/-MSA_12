from fastapi import FastAPI, HTTPException
from data.books import Book, CreateBook

books_app = FastAPI()


books: list[Book] = [
    #Book(0, "Евгений Oнегин", "Александр Сегеевич Пушкин"),
    #Book(1, "Война и мир", "Лев Николаевич Толстой"),
    #Book(2, "Таинственный остров", "Жуль Верн"),
]

def add_book(content: CreateBook):
    _id = len(books)
    books.append(Book(_id, content.name, content.author))
    return


@books_app.get("/books")
async def get_all_books():
    return books


@books_app.get("/book/{_id}")
async def get_book_by_id(_id: int):
    result = [item for item in books if item.id == _id]
    if len(result) > 0:
        return result[0]

    return HTTPException(status_code=404, detail="Book wasn't found.")


@books_app.get("/__health")
async def check_service():
    return


@books_app.post("/book")
async def add_books(content: CreateBook):
    add_book(content)
    return books[-1]