from library import library_api
from library.controllers.BookController import BookController

bookController = BookController()


@library_api.route("/book", methods=["POST"])
def add_book():
    return bookController.create()


@library_api.route("/listBook", methods=["GET"])
def list_book():
    return bookController.all()


@library_api.route("/updateBook/<int:id>", methods=["PUT"])
def update_book(id):
    return bookController.update(id)


@library_api.route("/deleteBook/<int:id>", methods=["DELETE"])
def delete_book(id):
    return bookController.delete(id)
