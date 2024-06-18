from extensions import db


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    statut = db.Column(db.String(25), nullable=False)
