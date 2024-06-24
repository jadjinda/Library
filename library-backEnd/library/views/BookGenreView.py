from library import library_api
from library.controllers.BookGenreController import BookGenreController
from flask_jwt_extended import jwt_required

bookGenreController = BookGenreController()


@jwt_required(refresh=True)
@library_api.route("/genre", methods=["POST"])
def add_genre():
    return bookGenreController.create()


@jwt_required(refresh=True)
@library_api.route("/listGenre", methods=["GET"])
def list_genre():
    return bookGenreController.all()


@jwt_required(refresh=True)
@library_api.route("/updateGenre/<int:id>", methods=["PUT"])
def update_genre(id):
    return bookGenreController.update(id)


@jwt_required(refresh=True)
@library_api.route("/deleteGenre/<int:id>", methods=["DELETE"])
def delete_genre(id):
    return bookGenreController.delete(id)
