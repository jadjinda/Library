import datetime
import uuid

from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from functools import wraps
from authentication.models.User import User
from extensions import db
import app


class UserController:
    def __init__(self):
        self.user_model = User

    def login(self):
        auth = request.authorization

        if not auth or not auth.email or not auth.password:
            return make_response('Could not verify', 401, {
                'WWW-Authenticate': 'Basic realm="Login required!"'
            })

        user = User.query.filter_by(name=auth.email).first()

        if not user:
            return make_response('Could not verify', 401, {
                'WWW-Authenticate': 'Basic realm="Login required!"'
            })
        if check_password_hash(user.password, auth.password):
            token = jwt.encode({'public_id' : user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

            return jsonify({'token': token.decode('UTF-8')})

        return make_response('Could not verify', 401, {
            'WWW-Authenticate': 'Basic realm="Login required!"'
        })

    def token_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
            if not token:
                return jsonify({'message': 'Token is missing!'}), 401
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'])
                current_user = User.query.filter_by(public_id=data['public_id']).first
            except:
                return jsonify({'message': 'Token is invalid!'}), 401

            return f(current_user, *args, **kwargs)

        return decorated

    def register(self):
        try:
            data = request.get_json()
            hashed_password = generate_password_hash(data['password'], method='sha256')

            user = self.user_model(public_id=str(uuid.uuid4()),
                                   firstname=data['firstname'],
                                   username=data['username'],
                                   email=data['email'],
                                   password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return jsonify({'message': 'Utilisateur créée avec success'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

