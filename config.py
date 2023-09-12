import os
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
 
db = SQLAlchemy()
admin = Admin()

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = 'static/uploads/'

class Config:
    db = SQLAlchemy()
    admin = Admin()
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
