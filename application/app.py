from flask import Flask

# import flask_whooshalchemy as wa

from extensions import db, guard, cors
from api import api
from config import Config
from models import Post
from models import User

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
