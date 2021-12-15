from flask_sqlalchemy import SQLAlchemy
import flask_praetorian
import flask_cors

db = SQLAlchemy()
guard = flask_praetorian.Praetorian()
cors = flask_cors.CORS()