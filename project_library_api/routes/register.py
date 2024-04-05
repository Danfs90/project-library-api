from flask import request
from flask.blueprints import Blueprint
from project_library_api.resources.user import User
from project_library_api import db

actions = Blueprint('user', 'user', url_prefix='/v1/user')

@actions.route('/register', methods=['POST'])
def login():
    """Rota responsavel pelo login do usuario"""
    
    data = request.json
    
    username = data.get('username')
    password = data.get('password')
    birth_date = data.get('birth_date')
    address = data.get('address')
    zip_code = data.get('zip_code')
    role = data.get('role')    

    new_user = User(
        username=username,
        password=password,
        db=db.session,
        birth_date=birth_date,
        address=address,
        zip_code=zip_code,
        role=role
        )
    
    login_response = new_user.create_registration()
    return login_response, 200
