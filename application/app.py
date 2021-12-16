from flask import Flask
from application.extensions import db
from application.api import api
from application.config import Config
from application.models import Post
from flask_msearch import Search



def create_app(config=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    db.init_app(app)
    app.register_blueprint(api)
    search = Search(app)
    search.init_app(app)
    # search.create_index(update=True)
    with app.app_context():
        db.create_all()
        db.session.commit()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
