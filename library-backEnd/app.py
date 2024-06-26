from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from extensions import db
from library import library_api
from authentication import authentication_api

app = Flask(__name__)
CORS(app, origins="*")

#Blueprint Configuration
app.register_blueprint(library_api, url_prefix='/library')
app.register_blueprint(authentication_api, url_prefix='/auth')

#Folder Configuration
app.config['SECRET_KEY'] = 'key_secret'
app.config['BASE_TEMPLATE_FOLDER'] = 'library/templates'

#Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://josue:1234Jojo@127.0.0.1:3306/libraryManage'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Jwt Configuration
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)

db.init_app(app)
migrate = Migrate(app, db)
