from flask import Flask
from flask_cors import CORS
from project_library_api import config
from project_library_api.routes import auth, register, books, my_books
from project_library_api import db

app = Flask(__name__)
app.config.from_object(config)

#Abre a conexão do banco
db.init_app(app)

#CORS
CORS(app)

#Rotas
app.register_blueprint(auth.actions)
app.register_blueprint(register.actions)
app.register_blueprint(books.actions)
app.register_blueprint(my_books.actions)