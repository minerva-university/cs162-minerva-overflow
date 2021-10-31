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


def get_posts_written_by_user(user_id: int):
    return User.query.filter_by(user_id=user_id).first().posts


def get_user_favorite_posts(user_id: int):
    return User.query.filter_by(user_id=user_id).first().favorite_of


def get_comments_written_by_user(user_id: int):
    return User.query.filter_by(user_id=user_id).first().comments


def get_tag_posts(tag_id: int):
    return Tag.query.filter_by(tag_id=tag_id).first().posts


def get_posts_comments(post_id: int):
    return Post.query.filter_by(post_id=post_id).first().comments


def get_user_who_favorited_post(post_id: int):
    return Post.query.filter_by(post_id=post_id).first().favorite_of


def get_posts_tags(post_id: int):
    return Post.query.filter_by(post_id=post_id).first().tags


def get_users_from_cohort(cohort_id: int):
    return Cohort.query.filter_by(cohort_id=cohort_id).first().users


def get_posts_by_city(city_id: int):
    return City.query.filter_by(city_id=city_id).first().posts


if __name__ == '__main__':
    app.run()
