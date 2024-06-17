import flask
from flask_migrate import Migrate
from flask_cors import CORS

from authentication import auth_api
from extensions import db
from library import libray_api

app = flask.Flask(__name__)
CORS(app, origins="*")

app.register_blueprint(libray_api, url_prefix='/library')
app.register_blueprint(auth_api, url_prefix='/auth')

app.config['SECRET_KEY'] = 'library_secret'
app.config['BASE_TEMPLATE_FOLDER'] = 'library/templates'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://josue:1234Jojo@127.0.0.1:3306/library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)