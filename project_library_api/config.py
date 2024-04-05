import os

APP_NAME = 'project-library-api'
APP_VERSION = '1.0.0'

SECRET_KEY_JWT = os.environ['SECRET_KEY_JWT']

SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']