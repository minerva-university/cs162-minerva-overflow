from flask import Flask

# import flask_whooshalchemy as wa

import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

from application.extensions import db
from application.api import api

# from application.config import Config
from application.models import Post


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # WHOOSH_BASE = "whoosh"
    SECRET_KEY = "192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf"
    SQLALCHEMY_DATABASE_URI = "sqlite:///"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


def create_app(config=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    db.init_app(app)
    app.register_blueprint(api)
    # wa.whoosh_index(app, Post)
    with app.app_context():
        db.create_all()
        db.session.commit()
    return app


if __name__ == "__main__":
    print(basedir)
    app = create_app()
    app.run()
