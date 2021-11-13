from flask import Flask

# import flask_whooshalchemy as wa

import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

from application.extensions import db
from application.api import api
from application.config import Config
from application.models import Post


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
