import jwt
import datetime
from project_library_api.util import hash_password
from project_library_api.config import SECRET_KEY_JWT
from project_library_api.models import Users

class Authentication():
    def __init__(self, email, password, db):
        self.db = db
        self.secret_key = SECRET_KEY_JWT
        self.email = email
        self.password = password

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload['email']
        except jwt.ExpiredSignatureError:
            return 'Token expirado. Faça login novamente.'
        except jwt.InvalidTokenError:
            return 'Token inválido. Faça login novamente.'

    def login(self):

        validate_login = self.check_credentials()

        if validate_login:
            return {'message': 'Login bem-sucedido', 'status': True}
        else:
            return {'message': 'Credenciais inválidas', 'status': False}

    def protected_route(self, token):
        username = self.verify_token(token)
        if username:
            return f'Bem-vindo, {username}! Esta é uma rota protegida.'
        else:
            return 'Token inválido ou expirado. Faça login novamente.'

    def check_credentials(self):

        hashed_password = hash_password(self.email, self.password)
        if hashed_password:
            db_hashed_password = self.db.query(Users.hash).filter(Users.hash == hashed_password).first()
        
        return hashed_password == db_hashed_password[0]

