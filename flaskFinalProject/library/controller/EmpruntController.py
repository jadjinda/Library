from library.models.Emprunt import Emprunt
from flask import jsonify, request
from extensions import db


class EmpruntController:
    def __init__(self):
        self.book_model = Emprunt

    def create(self):
        pass

    def all(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass