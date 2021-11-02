from flask import Flask, render_template, request, redirect, url_for, jsonify

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

"""
All of these route functions are not tested and given just for the reference of the other backend developers. Consider 
testing them, or rewriting them if needed.
"""


# Home page
@app.route("/add", methods=['POST'])
def index():
    return render_template('index.html')


@app.route("/add_user", methods=['POST'])
def add_user():
    """ Function to add user to the database """
    user = User(**request.form)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/add_post", methods=['POST'])
def add_post():
    """ Function to add post to the database """
    post = Post(**request.form)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/add_tag", methods=['POST'])
def add_tag():
    """ Function to add tag to the database """
    tag = Tag(**request.form)
    db.session.add(tag)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/add_tag_to_post/<tag_id>/<post_id>", methods=['POST'])
def add_tag_to_post(tag_id, post_id):
    """ Function to add tag to the post in the database """
    db.session.execute(tags_and_posts.insert().values(tag_id=tag_id, post_id=post_id))
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/edit_post/<post_id>", methods=['POST'])
def edit_post(post_id):
    """ Function to edit post in the database """
    post = Post.query.filter_by(post_id=int(post_id)).first()
    new_post_dict = request.form
    for item, value in post.__dict__.items():
        new_entry = new_post_dict.get(item)
        if new_entry and new_entry != value:
            setattr(post, item, new_entry)
    post.edited = True
    db.session.commit()

    return redirect(url_for('index'))


@app.route("/upvote_post/<post_id>", methods=['POST'])
def upvote_post(post_id):
    """ Function to upvote post """
    post = Post.query.filter_by(post_id=int(post_id)).first()
    post.upvotes += 1
    db.session.commit()

    return redirect(url_for('index'))


""" 
All functions below are utility functions that can be used in the route functions to have an easy connection
with the database.
 """


def get_posts_written_by_user(user_id: int):
    return User.query.filter_by(user_id=user_id).first().posts


def get_user_favorite_posts(user_id: int):
    return User.query.filter_by(user_id=user_id).first().user_favorite_posts


def get_comments_written_by_user(user_id: int):
    return User.query.filter_by(user_id=user_id).first().comments


def get_tag_posts(tag_id: int):
    return Tag.query.filter_by(tag_id=tag_id).first().posts


def get_posts_comments(post_id: int):
    return Post.query.filter_by(post_id=post_id).first().comments


def get_user_who_favorited_post(post_id: int):
    return Post.query.filter_by(post_id=post_id).first().favorite_of


def get_post_tags(post_id: int):
    return Post.query.filter_by(post_id=post_id).first().tags


def get_users_from_cohort(cohort_id: int):
    return Cohort.query.filter_by(cohort_id=cohort_id).first().users


def get_posts_by_city(city_id: int):
    return City.query.filter_by(city_id=city_id).first().posts


def create_app():
    db.init_app(app)
    db.create_all()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
