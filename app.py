from flask import Flask


#import flask_whooshalchemy as wa

from application.extensions import db
from application.api import api
from application.config import Config
from application.models import Post
from flask.helpers import send_from_directory

app = Flask(__name__, static_folder='frontend/build', static_url_path='')
app.config.from_object(Config)
app.app_context().push()
db.init_app(app)
app.register_blueprint(api)
# wa.whoosh_index(app, Post)
with app.app_context():
    db.create_all()
    db.session.commit()

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run()

