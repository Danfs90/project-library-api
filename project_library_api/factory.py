from project_library_api import db

def new_register(first_name, last_name, cellphone, email, password, birth_date, address, zip_code, role):
    from project_library_api.resources.user import User

    return User(first_name=first_name, last_name=last_name, cellphone=cellphone, email=email, password=password,\
         db=db.session, birth_date=birth_date, address=address, zip_code=zip_code, role=role)

def new_login(hash, db):
    from project_library_api.resources.auth import Authentication

    return Authentication(hash=hash, db=db)