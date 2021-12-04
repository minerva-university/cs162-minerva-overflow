from flask import Flask


#import flask_whooshalchemy as wa

from application.extensions import db
from application.api import api
from application.config import Config
from application.models import Post


app = Flask(__name__)
app.config.from_object(Config)
app.app_context().push()
db.init_app(app)
app.register_blueprint(api)
# wa.whoosh_index(app, Post)
with app.app_context():
    db.create_all()
    db.session.commit()



if __name__ == "__main__":
    app.run()

