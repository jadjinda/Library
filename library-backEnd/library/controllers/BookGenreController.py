from library.models.Genre import Genre
from flask import jsonify, request
from extensions import db


class BookGenreController:
    def __init__(self):
        self.genre_model = Genre

    def create(self):
        try:
            data = request.get_json()
            newGenre = self.genre_model(nom=data['nom'],
                                        statut=data['statut'])
            db.session.add(newGenre)
            db.session.commit()
            return jsonify({'message': 'Genre créée avec succès'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def all(self):
        try:
            genres = Genre.query.all()
            result = [{'id': genre.id,
                       'nom': genre.nom,
                       'statut': genre.statut} for genre in genres]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def update(self, bookGenre_id):
        try:
            data = request.get_json()
            genre = Genre.query.get(bookGenre_id)
            if genre:
                genre.nom = data['nom'],
                genre.statut = data['statut']
                db.session.commit()
                return jsonify({'message': 'Genre mise à jour avec succès'}), 200
            else:
                return jsonify({'message': 'Genre non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def delete(self, bookGenre_id):
        try:
            genre = Genre.query.get(bookGenre_id)
            if genre:
                db.session.delete(genre)
                db.session.commit()
                return jsonify({'message': 'Genre supprimée avec succès'}), 200
            else:
                return jsonify({'message': 'Genre non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500