from enum import Enum
from project_library_api import db

class Role(Enum):
    ADMIN = 'admin'
    USER = 'user'
    EMPLOYEE = 'employee'

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(125), unique=True, nullable=False)
    first_name = db.Column(db.String(30), unique=True, nullable=False)
    last_name = db.Column(db.String(50), unique=True, nullable=False)
    cellphone = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(125), unique=True, nullable=False)
    birth_date = db.Column(db.DateTime(), nullable=False)
    address = db.Column(db.String(125), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False, default=Role.USER)
    number = db.Column(db.String(10), nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'hash': self.hash,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'cellphone': self.cellphone,
            'email': self.email,
            'birth_date': self.birth_date.strftime('%Y-%m-%d'),
            'address': self.address,
            'zip_code': self.zip_code,
            'role': self.role.value,
            'number': self.number
        }
