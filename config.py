import os
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
 
db = SQLAlchemy()
admin = Admin(name='The Dawgs Admin', template_mode='bootstrap3')

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = 'static/uploads/'

class DBConfig:
    db_type = os.getenv("DB_TYPE", "postgresql")
    user = os.getenv("DB_USER", "DB_USER")
    passwd = os.getenv("DB_PASSWD", "DB_PASSWD")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", 5432)
    db_name = os.getenv("DB_NAME", "thebigda_tbd")
    db_uri = f"postgresql://{user}:{passwd}@{host}:{port}/{db_name}"

class Config:
    db = SQLAlchemy()
    admin = Admin()
    SECRET_KEY = os.environ.get('SECRET_KEY')
    db_type = os.getenv("DB_TYPE", "postgresql")
    user = os.getenv("DB_USER", "DB_USER")
    passwd = os.getenv("DB_PASSWD", "DB_PASSWD")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", 5432)
    db_name = os.getenv("DB_NAME", "thebigda_tbd")
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI", DBConfig.db_uri)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_QUERY_TIMEOUT = 0.1  # log the slow database query, and unit is second
    SQLALCHEMY_RECORD_QUERIES = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get(f"postgresql://{user}:{passwd}@{host}:{port}/{db_name}")\
    #     or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # db_uri = (
    #     f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8mb4"
    # )