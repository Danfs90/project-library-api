import jwt
import datetime
from project_library_api.util import hash_password
from project_library_api.config import SECRET_KEY_JWT
from project_library_api.models import Users

class Authentication():
    def __init__(self, hash, db):
        self.db = db
        self.secret_key = SECRET_KEY_JWT
        self.hash = hash
   

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

            return {'message': 'Login bem-sucedido',
                     'data': {
                      'user_id':validate_login[1],
                      'role':validate_login[2].value  
                     }}, 200
        
        else:
            return {'message': 'Credenciais inválidas', 'data': False}, 403

    def protected_route(self, token):
        username = self.verify_token(token)
        if username:
            return f'Bem-vindo, {username}! Esta é uma rota protegida.'
        else:
            return 'Token inválido ou expirado. Faça login novamente.'

    def check_credentials(self):
        """Funcao para validacao de login"""

        db_hashed_password = self.db.query(Users.hash, Users.id, Users.role).filter(Users.hash == self.hash).first()

        if db_hashed_password:

            return db_hashed_password

        return False

