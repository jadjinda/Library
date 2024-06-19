from flask import Blueprint

authentication_api = Blueprint('authentication_api', __name__, template_folder='templates', static_folder='static')

from authentication.views import UserView
