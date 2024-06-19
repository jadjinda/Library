from library import library_api
from library.controllers.BookGenreController import BookGenreController

bookGenreController = BookGenreController()


@library_api.route("/genre", methods=["POST"])
def add_genre():
    return bookGenreController.create()


@library_api.route("/listGenre", methods=["GET"])
def list_genre():
    return bookGenreController.all()


@library_api.route("/updateGenre/<int:id>", methods=["PUT"])
def update_genre(id):
    return bookGenreController.update(id)


@library_api.route("/deleteGenre/<int:id>", methods=["DELETE"])
def delete_genre(id):
    return bookGenreController.delete(id)
