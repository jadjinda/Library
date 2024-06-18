from library import library_api
from library.controllers.BookCategoryController import BookCategoryController

bookCategoryController = BookCategoryController()


@library_api.route("/category", methods=["POST"])
def add_category():
    return bookCategoryController.create()


@library_api.route("/listCategory", methods=["GET"])
def list_category():
    return bookCategoryController.all()


@library_api.route("/updateCategory/<int:id>", methods=["PUT"])
def update_category(id):
    return bookCategoryController.update(id)


@library_api.route("/deleteCategory/<int:id>", methods=["DELETE"])
def delete_category(id):
    return bookCategoryController.delete(id)