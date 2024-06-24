from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from authentication.models.User import User
from extensions import db


class UserController:
    def __init__(self):
        self.model = User

    def login(self, email, password):
        user = self.model.query.filter_by(username=email).first()

        if user is not None:
            if user.verify_password(password):
                access_token = create_access_token(identity=email)
                refresh_token = create_refresh_token(identity=email)
                return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200
            else:
                return jsonify({"msg": "Bad username or password"}), 401
        else:
            return jsonify({"msg": "Bad username or password"}), 401

    def logout(self):
        pass

    #def register(self, firstname, username, email, password):
    #    user = self.model(firstname=firstname, username=username, email=email, password=password)
    #    user.password = password
    #    db.session.add(user)
    #    db.session.commit()
    #    return jsonify({"msg": "User created successfully"}), 201

    def register(self):
        try:
            data = request.get_json()
            newUser = self.model(firstname=data['firstname'],
                                 username=data['username'],
                                 email=data['email'],
                                 password=data['password'])
            db.session.add(newUser)
            db.session.commit()
            return jsonify({'message': 'Utilisateur créée avec succès'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
