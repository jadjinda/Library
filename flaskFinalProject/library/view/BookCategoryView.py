from library import libray_api
from library.controller.BookCategoryController import BookCategoryController

bookCategoryController = BookCategoryController()


@libray_api.route("/category", methods=["POST"])
def add_book():
    bookCategoryController.create()


@libray_api.route("/listCategory", methods=["GET"])
def list_book():
    bookCategoryController.all()


@libray_api.route("/updateCategory/<int:id>", methods=["PUT"])
def update_book(id):
    bookCategoryController.update(id)


@libray_api.route("/deleteCategory/<int:id>", methods=["DELETE"])
def delete_book(id):
    bookCategoryController.delete(id)