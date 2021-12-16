from flask import Flask

# import flask_whooshalchemy as wa

from application.extensions import db, guard, cors
from application.api import api
from config import Config
from application.models import User


def create_app(config=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    db.init_app(app)
    guard.init_app(app, User)
    cors.init_app(app)
    app.register_blueprint(api)
    # wa.whoosh_index(app, Post)
    with app.app_context():
        db.create_all()
        db.session.commit()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
