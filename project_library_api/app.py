from flask import Flask
from flask_cors import CORS

from project_library_api import config
from project_library_api.routes import auth

app = Flask(__name__)
app.config.from_object(config)

#CORS
CORS(app)

#Rotas
app.register_blueprint(auth.actions)