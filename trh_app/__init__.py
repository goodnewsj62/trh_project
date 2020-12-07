from flask import Flask, request, url_for, abort, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from configuration.config import Config


db = SQLAlchemy()
migrate = Migrate()
bcrypt_ = Bcrypt()
login_manager = LoginManager()
login_manager.login_message_category = 'info'


def create_app(config_file=Config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_file)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt_.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from .admin.manager import auth
        from .blog.app import blog

        app.register_blueprint(blog)
        app.register_blueprint(auth)

        return app
