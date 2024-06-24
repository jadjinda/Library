from flask import request
from authentication import authentication_api
from authentication.controllers.UserController import UserController

userController = UserController()


@authentication_api.route("/login", methods=["POST"])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    print(email, password)
    return userController.login(email, password)


@authentication_api.route("/register", methods=["POST"])
def register():
    firstname = request.json.get('firstname', None)
    username = request.json.get('username', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    return userController.register()
