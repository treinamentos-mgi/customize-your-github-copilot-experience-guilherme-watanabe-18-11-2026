from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str
    author: str
    year: int


books: dict[int, BookInput] = {}
next_book_id = 1


@app.get("/books")
def list_books():
    return [
        {"id": book_id, **book.model_dump()}
        for book_id, book in books.items()
    ]


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookInput):
    # TODO: Store the book and return it with its assigned ID.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find the book or raise an HTTP 404 error.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    # TODO: Replace the existing book or raise an HTTP 404 error.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Remove the book or raise an HTTP 404 error, then return an empty response.
    return Response(status_code=status.HTTP_204_NO_CONTENT)