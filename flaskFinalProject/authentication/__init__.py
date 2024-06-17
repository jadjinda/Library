from flask import Blueprint

auth_api = Blueprint('url', __name__, template_folder='templates', static_folder='static')