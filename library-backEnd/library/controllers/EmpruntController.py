from library.models.Emprunt import Emprunt
from flask import jsonify, request
from extensions import db


class EmpruntController:
    def __init__(self):
        self.emprunt_model = Emprunt

    def create(self):
        try:
            nomEmprunteur = request.form['nomEmprunteur']
            dateEmprunt = request.form['dateEmprunt']
            dateRetour = request.form['dateRetour']
            observation = request.form['observation']
            livre_id = request.form['livre_id']

            emprunt = self.emprunt_model(nomEmprunteur=nomEmprunteur,
                                   dateEmprunt=dateEmprunt,
                                   dateRetour=dateRetour,
                                   observation=observation,
                                   livre_id=livre_id)
            db.session.add(emprunt)
            db.session.commit()
            return jsonify({'message': 'Emprunt créée avec succès'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def all(self):
        try:
            emprunts = self.emprunt_model.query.all()
            result = [{'id': emprunt.id,
                       'nomEmprunteur': emprunt.nomEmprunteur,
                       'dateEmprunt': emprunt.dateEmprunt,
                       'dateRetour': emprunt.dateRetour,
                       'observation': emprunt.observation} for emprunt in emprunts]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def update(self, emprunt_id):
        pass

    def delete(self, emprunt_id):
        try:
            emprunt = Emprunt.query.get(emprunt_id)
            if emprunt:
                db.session.delete(emprunt)
                db.session.commit()
                return jsonify({'message': 'Emprunt supprimée avec succès'}), 200
            else:
                return jsonify({'message': 'Emprunt non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500