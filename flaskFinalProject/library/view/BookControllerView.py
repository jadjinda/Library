from library import libray_api
from library.controller.BookController import BookController

bookController = BookController()


@libray_api.route("/book", methods=["POST"])
def add_book():
    bookController.create()


@libray_api.route("/listBook", methods=["GET"])
def list_book():
    bookController.all()


@libray_api.route("/update/<int:id>", methods=["PUT"])
def update_book(id):
    bookController.update(id)


@libray_api.route("/delete/<int:id>", methods=["DELETE"])
def delete_book(id):
    bookController.delete(id)
