from flask import Blueprint

library_api = Blueprint('library_api', __name__, template_folder='templates', static_folder='static')

from library.views import BookCategoryView, BookView, EmpruntView, BookGenreView
