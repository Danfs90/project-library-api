from project_library_api import db

class UsersBooks(db.Model):
    __tablename__ = 'users_books'

    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    id_book = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)

    user = db.relationship('Users', backref=db.backref('users_books', cascade='all, delete-orphan'))
    book = db.relationship('Book', backref=db.backref('users_books', cascade='all, delete-orphan'))
