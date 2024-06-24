from library import library_api
from library.controllers.BookCategoryController import BookCategoryController
from flask_jwt_extended import jwt_required

bookCategoryController = BookCategoryController()


@jwt_required(refresh=True)
@library_api.route("/category", methods=["POST"])
def add_category():
    return bookCategoryController.create()


@jwt_required(refresh=True)
@library_api.route("/listCategory", methods=["GET"])
def list_category():
    return bookCategoryController.all()


@jwt_required(refresh=True)
@library_api.route("/updateCategory/<int:id>", methods=["PUT"])
def update_category(id):
    return bookCategoryController.update(id)


@jwt_required(refresh=True)
@library_api.route("/deleteCategory/<int:id>", methods=["DELETE"])
def delete_category(id):
    return bookCategoryController.delete(id)
