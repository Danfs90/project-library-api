
import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

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
