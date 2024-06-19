import logging

from project_library_api.models import Users
from project_library_api import db
from flask import request
from flask.blueprints import Blueprint
from project_library_api.factory import new_register
from project_library_api.util import api_response

LOGGER = logging.getLogger(__name__)

actions = Blueprint('user', 'user', url_prefix='/v1/user')

@actions.route('/register', methods=['POST'])
def login():
    """Rota responsavel pelo login do usuario"""
    try:
        data = request.json
        
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        cellphone = data.get('cellphone')
        email = data.get('email')
        password = data.get('password')
        birth_date = data.get('birth_date')
        address = data.get('address')
        zip_code = data.get('zip_code')
        role = data.get('role')    
        
        if (not first_name) and (not email) and (not password) and (not role):
            LOGGER.info('Parametros de user, password ou role não enviados na requisição')
            return api_response(400, message="Parametros obrigatorios não enviados na requisição")
        
        new_user = new_register(first_name, last_name, cellphone, email,\
                             password, birth_date, address, zip_code, role)
        
        login_response = new_user.create_registration()

        return api_response(data=login_response, status_code=200, message="Usuario criado com sucesso!")
    except Exception as ex:
        return api_response(500, message="Erro interno no servidor")
    
@actions.route('/update', methods=['PUT'])
def login_add():
    """Rota responsavel pela alteração """
    try:
        data = request.json
        
        id_user = data.get('id_user')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        cellphone = data.get('cellphone')
        email = data.get('email')
        birth_date = data.get('birth_date')
        address = data.get('address')
        zip_code = data.get('zip_code')
        role = data.get('role')    

        user = db.session.query(Users).filter(Users.id == id_user).first()
        
        user.first_name = first_name if first_name else user.first_name
        user.last_name = last_name if last_name else user.last_name
        user.cellphone = cellphone if cellphone else user.cellphone
        user.birth_date = birth_date if birth_date else user.birth_date
        user.zip_code = zip_code if zip_code else user.zip_code
        user.role = role if role else user.role
        user.email = email if email else user.address
        user.address = address if address else user.address

        db.session.commit()

        return api_response(data='Usuario ajustado com sucesso!', status_code=200, message="Usuario criado com sucesso!")
    except Exception as ex:
        return api_response(500, message="Erro interno no servidor")    