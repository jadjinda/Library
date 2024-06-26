from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
from authentication.models.User import User
from extensions import db


class UserController:
    def __init__(self):
        self.model = User

    def register(self):
        data = request.get_json()
        new_user = self.model(firstname=data['firstname'],
                              username=data['username'],
                              email=data['email'],
                              password=generate_password_hash(data['password']))
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message="User created successfully"), 201

    def login(self):
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()

        if user and check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity={'username': user.username})
            return jsonify(access_token=access_token)
        else:
            return jsonify(message="Invalid credentials"), 401
