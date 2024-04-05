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
    username = db.Column(db.String(125), unique=True, nullable=False)
    birth_date = db.Column(db.DateTime(), nullable=False)
    address = db.Column(db.String(125), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False, default=Role.USER)
    number = db.Column(db.String(10), nullable=False)
