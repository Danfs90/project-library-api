
import hashlib
from project_library_api.models import Users
from datetime import datetime
class User:
    def __init__(self, username, password, db = None, birth_date = None, address = None, zip_code = None, role = None, number = None):
        self.db = db
        self.username = username
        self.password = password
        self.birth_date = birth_date
        self.address = address
        self.zip_code = zip_code
        self.role = role
        self.number = number

    def create_registration(self):
        #TODO Adicionar algumas validações
        
        new_user = Users()

        new_user.username = self.username
        new_user.hash = self._hash_password(self.password)
        new_user.birth_date = datetime.strptime(self.birth_date, '%Y-%m-%dT%H:%M:%S.%fZ')
        new_user.address = self.address
        new_user.zip_code = self.zip_code
        new_user.role = self.role
        new_user.number = self.number

        self.db.add(new_user)
        self.db.commit()
        
    def _hash_password(self, password):
        """Função responsavel para criar a hash de usuario e senha"""
        hash_string = self.username + password
        hashed_password = hashlib.sha256(hash_string.encode()).hexdigest()
        return hashed_password
    
    def check_credentials(self, username, password):

        hashed_password = self._hash_password(password)
        if hashed_password:
            pass
            #TODO criar validação de banco aqui
        
        return self.username == username and self.password == password
