from library.models.Book import Book
from flask import jsonify, request
from extensions import db


class BookController:
    def __init__(self):
        self.book_model = Book

    def create(self):
        try:
            titre = request.form['titre']
            auteur = request.form['auteur']
            codeISBN = request.form['codeISBN']
            datePublication = request.form['datePublication']
            nombreExemplaires = request.form['nombreExemplaires']
            genre_id = request.form['genre_id']
            category_id = request.form['category_id']

            if 'imageCouverture' not in request.files:
                return jsonify({'message': 'Aucun fichier image'}), 400
            imageCouverture = request.files['imageCouverture']
            book = self.book_model(titre=titre,
                                   auteur=auteur,
                                   codeISBN= codeISBN,
                                   datePublication= datePublication,
                                   nombreExemplaires= nombreExemplaires,
                                   genre_id = genre_id,
                                   category_id= category_id)
            book.save_image(imageCouverture)
            db.session.add(book)
            db.session.commit()
        except KeyError:
            return jsonify({'message': 'Donnée manquant'}), 400
        except Exception as e:
            return jsonify({'message': e}), 500

    def all(self):
        try:
            books = self.book_model.query.all()
            result = [{'id': book.id,
                       'titre': book.titre,
                       'auteur': book.auteur,
                       'codeISBN': book.codeISBN,
                       'datePublication': book.datePublication,
                       'nombreExemplaires': book.nombreExemplaires,
                       'imageCouverture': book.imageCouverture} for book in books]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def update(self, book_id):
        try:
            data = request.get_json()
            book = Book.query.get(book_id)
            if book:
                book.titre = data['libelle'],
                book.auteur = data['auteur'],
                book.codeISBN = data['codeISBN'],
                book.datePublication = data['datePublication'],
                book.nombreExemplaires = data['nombreExemplaires'],
                book.imageCouverture = data['imageCouverture'],
                book.genre_id = data['genre_id'],
                book.category_id = data['category_id']
                db.session.commit()
                return jsonify({'message': 'Livre mise à jour avec succès'}), 200
            else:
                return jsonify({'message': 'Livre non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def delete(self, book_id):
        try:
            book = Book.query.get(book_id)
            if book:
                db.session.delete(book)
                db.session.commit()
                return jsonify({'message': 'Livre supprimée avec succès'}), 200
            else:
                return jsonify({'message': 'Livre non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500