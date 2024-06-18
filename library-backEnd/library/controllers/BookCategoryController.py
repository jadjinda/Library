from library.models.Category import Category
from flask import jsonify, request
from extensions import db


class BookCategoryController:
    def __init__(self):
        self.category_model = Category

    def create(self):
        try:
            data = request.get_json()
            newCategory = self.category_model(nom=data['nom'],
                                              description=data['description'],
                                              statut=data['statut'])
            db.session.add(newCategory)
            db.session.commit()
            return jsonify({'message': 'Catégorie créée avec succès'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def all(self):
        try:
            categories = Category.query.all()
            result = [{'id': bookCategory.id,
                       'nom': bookCategory.nom,
                       'description': bookCategory.description,
                       'statut': bookCategory.statut} for bookCategory in categories]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def update(self,bookCategory_id):
        try:
            data = request.get_json()
            category = Category.query.get(bookCategory_id)
            if category:
                category.nom = data['nom'],
                category.description = data['statut'],
                category.statut = data['statut']
                db.session.commit()
                return jsonify({'message': 'Catégorie mise à jour avec succès'}), 200
            else:
                return jsonify({'message': 'Catégorie non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Donées manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message':e}), 500

    def delete(self,bookCategory_id):
        try:
            category = Category.query.get(bookCategory_id)
            if category:
                db.session.delete(category)
                db.session.commit()
                return jsonify({'message': 'Catégorie supprimée avec succès'}), 200
            else:
                return jsonify({'message': 'Catégorie non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
