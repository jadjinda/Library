from flask import Blueprint

libray_api = Blueprint('app', __name__, template_folder='templates', static_folder='static')