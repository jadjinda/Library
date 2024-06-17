from library.models.Category import Category
from flask import jsonify, request
from extensions import db


class BookCategoryController:
    def __init__(self):
        self.book_model = Category

    def create(self):
        pass

    def all(self):
        try:
            categories = Category.query.all()
            result = [{'id': bookCategory.id,
                       'nom': bookCategory.nom,
                       'description': bookCategory.description,
                       'statut': bookCategory.statut} for bookCategory in categories]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def update(self, book_id):
        pass

    def delete(self, book_id):
        pass