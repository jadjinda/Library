from library import library_api
from library.controllers.EmpruntController import EmpruntController

empruntController = EmpruntController()

@library_api.route("/emprunt", methods=["POST"])
def add_emprunt():
    return empruntController.create()


@library_api.route("/listEmprunt", methods=["GET"])
def list_emprunt():
    return empruntController.all()


@library_api.route("/updateEmprunt/<int:id>", methods=["PUT"])
def update_emprunt(id):
    return empruntController.update(id)


@library_api.route("/deleteEmprunt/<int:id>", methods=["DELETE"])
def delete_emprunt(id):
    return empruntController.delete(id)