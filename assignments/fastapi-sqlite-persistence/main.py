import sqlite3
from contextlib import contextmanager
from typing import Iterator

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

DATABASE_PATH = "books.db"
app = FastAPI(title="Books API with SQLite")


class BookInput(BaseModel):
    title: str
    author: str
    year: int


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database() -> None:
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL
            )
            """
        )


initialize_database()


@app.get("/books")
def list_books():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, title, author, year FROM books ORDER BY id"
        ).fetchall()
    return [dict(row) for row in rows]


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookInput):
    # TODO: Insert the book using SQL parameters and return it with its ID.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Query by ID and raise HTTPException with status 404 if missing.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    # TODO: Update by ID using SQL parameters; return 404 if no row was updated.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Delete by ID and return 404 if no row was deleted.
    return Response(status_code=status.HTTP_204_NO_CONTENT)