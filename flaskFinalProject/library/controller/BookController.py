from library.models.Book import Book
from flask import jsonify, request
from extensions import db


class BookController:
    def __init__(self):
        self.book_model = Book

    def create(self):
        pass

    def all(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
