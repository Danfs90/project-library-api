import logging

from flask import request
from project_library_api import db 
from flask.blueprints import Blueprint
from project_library_api.util import api_response
from project_library_api.models.users_books import UsersBooks
from project_library_api.models.books import Book

LOGGER = logging.getLogger(__name__)

actions = Blueprint('my_books', 'my_books', url_prefix='/v1/my_books')

@actions.route('/<id_user>', methods=['GET'])
def my_books(id_user):
    """Rota responsavel pelo login do usuario"""
    try:
        
        if (not id_user):
            LOGGER.info('Parametros de user, password ou role não enviados na requisição')
            return api_response(400, message="Parametros obrigatorios não enviados na requisição")
        

        id_books = db.session.query(UsersBooks).filter(UsersBooks.id_user == int(id_user)).all()

        if not id_books:
            LOGGER.info('Não localizados livros para o usuario: {}'.format(id_user))
            return api_response(403, message="Não localizados livros para o usuario")
        
        data_books = []
        for ids in id_books:
            
            books = db.session.query(Book).filter(Book.id == ids.id_book).all()

            if books:
                for book in books:
                    serialize_book = book.serialize()
                    data_books.append(serialize_book)


        return api_response(data=data_books, status_code=200, message="Livros localizados!")
    except Exception as ex:
        return api_response(500, message="Erro interno no servidor")