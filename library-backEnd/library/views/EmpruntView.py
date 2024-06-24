from library import library_api
from library.controllers.EmpruntController import EmpruntController
from flask_jwt_extended import jwt_required

empruntController = EmpruntController()


@jwt_required(refresh=True)
@library_api.route("/emprunt", methods=["POST"])
def add_emprunt():
    return empruntController.create()


@jwt_required(refresh=True)
@library_api.route("/listEmprunt", methods=["GET"])
def list_emprunt():
    return empruntController.all()


@jwt_required(refresh=True)
@library_api.route("/updateEmprunt/<int:id>", methods=["PUT"])
def update_emprunt(id):
    return empruntController.update(id)


@jwt_required(refresh=True)
@library_api.route("/deleteEmprunt/<int:id>", methods=["DELETE"])
def delete_emprunt(id):
    return empruntController.delete(id)
