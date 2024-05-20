
from project_library_api.models import Users
from project_library_api.util import hash_password
from datetime import datetime
class User:
    def __init__(self, first_name, last_name, cellphone, email, password, db, role, birth_date = None, address = None, zip_code = None, number = None):
        self.db = db
        self.first_name = first_name
        self.last_name = last_name
        self.cellphone = cellphone
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.address = address
        self.zip_code = zip_code
        self.role = role
        self.number = number

    def create_registration(self):
        
        new_user = Users()

        new_user.first_name = self.first_name
        new_user.last_name = self.last_name
        new_user.cellphone = self.cellphone
        new_user.email = self.email
        new_user.hash = hash_password(self.email, self.password)
        new_user.birth_date = datetime.strptime(self.birth_date, '%Y-%m-%dT%H:%M:%S.%fZ')
        new_user.address = self.address
        new_user.zip_code = self.zip_code
        new_user.role = self.role
        new_user.number = self.number

        self.db.add(new_user)
        self.db.commit()
        

    
