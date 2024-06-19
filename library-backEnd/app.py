from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from extensions import db
from library import library_api
from authentication import authentication_api

app = Flask(__name__)
CORS(app, origins="*")

app.register_blueprint(library_api, url_prefix='/library')
app.register_blueprint(authentication_api, url_prefix='/auth')

app.config['SECRET_KEY'] = 'key_secret'
app.config['BASE_TEMPLATE_FOLDER'] = 'library/templates'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://josue:1234Jojo@127.0.0.1:3306/libraryManage'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)