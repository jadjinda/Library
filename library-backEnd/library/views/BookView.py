from library import library_api
from library.controllers.BookController import BookController
from flask_jwt_extended import jwt_required

bookController = BookController()


@jwt_required(refresh=True)
@library_api.route("/book", methods=["POST"])
def add_book():
    return bookController.create()


@jwt_required(refresh=True)
@library_api.route("/listBook", methods=["GET"])
def list_book():
    return bookController.all()


@jwt_required(refresh=True)
@library_api.route("/updateBook/<int:id>", methods=["PUT"])
def update_book(id):
    return bookController.update(id)


@jwt_required(refresh=True)
@library_api.route("/deleteBook/<int:id>", methods=["DELETE"])
def delete_book(id):
    return bookController.delete(id)
