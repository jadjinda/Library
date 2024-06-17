from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(100))
    email = db.Column(db.String(50))
    password = db.Column(db.String(80))