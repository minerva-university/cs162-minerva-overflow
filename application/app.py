from flask import Flask, render_template, request, redirect, url_for, jsonify

from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *


# Home page
@app.route("/add", methods=['POST'])
def index():
    return render_template('index.html')


@app.route("/add_user", methods=['POST'])
def add_user():
    user = User(**request.form)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/add_post", methods=['POST'])
def add_post():
    post = Post(**request.form)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/add_tag", methods=['POST'])
def add_tag():
    tag = Tag(**request.form)
    db.session.add(tag)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
