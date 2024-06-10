import logging

from flask import request
from flask.blueprints import Blueprint
from project_library_api import db
from project_library_api.models import Book
from project_library_api.util import api_response

LOGGER = logging.getLogger(__name__)

actions = Blueprint('books', 'books', url_prefix='/v1/books')

@actions.route('/query', methods=['GET'])
def books_query():
    """Rota responsavel pelo retorno de todos os livros com estoque disponivel"""
    try:
        
        LOGGER.info("Verificando os livros disponiveis")

        books = db.session.query(Book).filter(Book.stock > 0).all()

        if books:
            serialized_books = [book.serialize() for book in books]

            return api_response(data=serialized_books, message='Livros localizados com sucesso!', status_code=200)
        
        return api_response(data=None, message='Livros não localizados!', status_code=404 )
    
    except Exception as e:
        LOGGER.info("Erro na autenticação do usuario: ".format(e))
        return api_response(data=None, message='Erro ao localizar os livro!', status_code=500)
    

@actions.route('/<book_id>', methods=['GET'])
def books_get(book_id):
    """Rota responsavel pelo retorno de um livro indicado pelo seu id"""
    try:
        
        LOGGER.info("Verificando os livros disponiveis")

        book = db.session.query(Book).filter(Book.id == book_id).first()

        if book:

            return api_response(data=[book.serialize()], message='Livro localizados com sucesso!', status_code=200)
        
        return api_response(data=None, message='Livro não localizados!', status_code=404 )
    
    except Exception as e:
        LOGGER.info("Erro na autenticação do usuario: ".format(e))
        return api_response(data=None, message='Erro ao localizar o livro!', status_code=500)
        
@actions.route('/<book_id>/delete', methods=['DELETE'])
def books_delete(book_id):
    """Rota responsavel por excluir livros"""
    try:
        
        LOGGER.info("Deletando o livro indicado")

        book = db.session.query(Book).filter(Book.id == book_id).first()

        if book:
            db.session.delete(book)
            db.session.commit()            

            return api_response(data=True, message='Livro deletado com sucesso!', status_code=200)
        
        return api_response(data=None, message='Livro não localizados!', status_code=404 )
    
    except Exception as e:
        LOGGER.info("Erro na autenticação do usuario: ".format(e))
        return api_response(data=None, message='Erro ao excluir o livro!', status_code=500 )
        
@actions.route('/add', methods=['POST'])
def books_add():
    """Rota responsavel por criar um novo livro"""
    try:
        
        LOGGER.info("Adicionando o novo licro")

        data = request.json

        new_book = Book(**data)

        db.session.add(new_book)

        db.session.commit()
        
        return api_response(data=[{'book_id':new_book.id}], message='Livro adicionado com sucesso!', status_code=200 )
    
    except Exception as e:
        LOGGER.info("Erro na autenticação do usuario: ".format(e))
        return api_response(data=False, message='Erro ao criar o novo livro!', status_code=500 )
                
@actions.route('/<book_id>/update', methods=['PUT'])
def books_update(book_id):
    """Rota responsavel por atualizar os dados do livro indicado na requisicao"""
    try:
        LOGGER.info("Adicionando o novo licro")
        book = db.session.query(Book).filter_by(id=book_id).first()
        if not book:
            return api_response(data=None, message='Livro não localizados!', status_code=404 )

        updated_data = request.json

        for key, value in updated_data.items():
            setattr(book, key, value)

        db.session.commit()
        return api_response(data=True, message='Livro alterado com sucesso!', status_code=200 )
    
    except Exception as e:
        LOGGER.info("Erro na autenticação do usuario: ".format(e))
        return api_response(data=False, message='Erro ao alterar o livro!', status_code=500 )
                        