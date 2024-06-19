from authentication import authentication_api
from authentication.controllers.UserController import UserController

userController = UserController()


@authentication_api.route("/login", methods=["POST"])
def add_category():
    return userController.login()


@authentication_api.route("/register", methods=["POST"])
def list_category():
    return userController.register()
