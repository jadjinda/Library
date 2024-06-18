from extensions import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    statut = db.Column(db.String(255), nullable=False)
