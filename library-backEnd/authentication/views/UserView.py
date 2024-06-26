from flask import request
from authentication import authentication_api
from authentication.controllers.UserController import UserController

userController = UserController()


@authentication_api.route("/login", methods=["POST"])
def login():
    return userController.login()


@authentication_api.route("/register", methods=["POST"])
def register():
    return userController.register()
