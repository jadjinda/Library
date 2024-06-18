import os
from extensions import db
from werkzeug.utils import secure_filename

upload_folder = 'library/static/image'
os.makedirs(upload_folder, exist_ok=True)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(255), nullable=False)
    auteur = db.Column(db.String(255), nullable=False)
    codeISBN = db.Column(db.String(255), nullable=False)
    datePublication = db.Column(db.Integer, nullable=False)
    nombreExemplaires = db.Column(db.Integer, nullable=False)
    imageCouverture = db.Column(db.String(255), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genre = db.relationship('Genre', backref=db.backref('book', lazy=True))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('book', lazy=True))

    def save_image(self, image_file):
        if image_file:
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(upload_folder, filename)
            image_file.save(image_path)
            self.image = filename
            db.session.commit()
