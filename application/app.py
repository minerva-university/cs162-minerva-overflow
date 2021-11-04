from flask import Flask

from application.config import Config
from application.models import *
from application.extensions import db
from application.api import api


def create_app(config=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    db.init_app(app)
    app.register_blueprint(api)
    with app.app_context():
        db.create_all()
        db.session.commit()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
