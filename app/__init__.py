from flask import Flask
from flask_admin import Admin
from config import Config, db, admin, UPLOAD_FOLDER 
from flask_ckeditor import CKEditor

ckeditor = CKEditor()

def create_app(config_class=Config):
    app = Flask(__name__)
    application = app
    app.config.from_object(config_class)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    # admin = Admin(app, name='TBDL', template_mode='bootstrap3')
    admin.init_app(app)
    app.config['FLASK_ADMIN_SWATCH'] = 'superhero'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    ckeditor.init_app(app)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app