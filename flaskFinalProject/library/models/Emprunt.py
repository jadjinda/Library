from extensions import db


class Emprunt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomEmprunteur = db.Column(db.String(255), nullable=False)
    dateEmprunt = db.Column(db.String(255), nullable=False)
    dateRetour = db.Column(db.String(255), nullable=False)
    observation = db.Column(db.String(255))
    livre_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    livre = db.relationship('Book', backref=db.backref('emprunt', lazy=True))