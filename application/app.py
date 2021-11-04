from config import Config
from flask import Flask, render_template, request, redirect, url_for, Response
from typing import List
from models import *
from extensions import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from application.forms import LoginForm, RegistrationForm


def create_app() -> Flask:
    application = Flask(__name__)
    application.config.from_object(Config)
    application.app_context().push()
    db.init_app(application)
    with application.app_context():
        db.create_all()
        db.session.commit()
    return application


app = create_app()


@app.route("/", methods=['POST'])
def index():
    return render_template('index.html')


@app.route("/users/add", methods=['POST'])
def add_user() -> Response:
    """ Function to add user to the database """
    user = User(**request.form)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/posts/add", methods=['POST'])
def add_post() -> Response:
    """ Function to add post to the database """
    post = Post(**request.form)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/tags/add", methods=['POST'])
def add_tag() -> Response:
    """ Function to add tag to the database """
    tag = Tag(**request.form)
    db.session.add(tag)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/posts/add_tag/<tag_id>/<post_id>", methods=['POST'])
def add_tag_to_post(tag_id: int, post_id: int) -> Response:
    """ Function to add tag to the post in the database """
    db.session.execute(tags_and_posts.insert().values(tag_id=tag_id, post_id=post_id))
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/posts/edit/<post_id>", methods=['POST'])
def edit_post(post_id: int) -> Response:
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


@app.route("/posts/upvote/<post_id>", methods=['POST'])
def upvote_post(post_id: int) -> Response:
    """ Function to upvote post """
    post = Post.query.filter_by(post_id=int(post_id)).first()
    post.upvotes += 1
    db.session.commit()

    return redirect(url_for('index'))


""" 
All functions below are utility functions that can be used in the route functions to have an easy connection
with the database.
 """


def get_posts_written_by_user(user_id: int) -> List[Post]:
    return User.query.filter_by(user_id=user_id).first().posts


def get_user_favorite_posts(user_id: int) -> List[Post]:
    return User.query.filter_by(user_id=user_id).first().user_favorite_posts


def get_comments_written_by_user(user_id: int) -> List[Comment]:
    return User.query.filter_by(user_id=user_id).first().comments


def get_tag_posts(tag_id: int) -> List[Post]:
    return Tag.query.filter_by(tag_id=tag_id).first().posts


def get_posts_comments(post_id: int) -> List[Comment]:
    return Post.query.filter_by(post_id=post_id).first().comments


def get_user_who_favorited_post(post_id: int) -> List[User]:
    return Post.query.filter_by(post_id=post_id).first().favorite_of


def get_post_tags(post_id: int) -> List[Tag]:
    return Post.query.filter_by(post_id=post_id).first().tags


def get_users_from_cohort(cohort_id: int) -> List[User]:
    return Cohort.query.filter_by(cohort_id=cohort_id).first().users


def get_posts_by_city(city_id: int) -> List[Post]:
    return City.query.filter_by(city_id=city_id).first().posts


def get_posts_by_cohoty(cohort_id: int) -> List[Post]:
    return Cohort.query.filter_by(cohort_id=cohort_id).first().posts


@app.route("/register", methods=['GET', 'POST'])
def register():
    #if the user is alredy aithenitificated then take them back to the home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    #get data form the registration form
    form = RegistrationForm()
    if form.validate_on_submit():
        #hash the password for security reasons
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #create an instance of a new user with their data in the database
        #NEEDS TO BE CHANGED
        #user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        #flash the message that the account has been created
        flash('Your account has been created! You are now able to log in', 'success')
        #and redirect the user to the login page
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        #if the user is alredy aithenitificated then take them back to the home page
        return redirect(url_for('home'))
    #get the data from the login form
    form = LoginForm()
    if form.validate_on_submit():
        #get information from the database that corresponds to data submited in the login form
        #NEEDS TO BE CHANGED
        user = User.query.filter_by(email=form.email.data).first()
        #if the user exists and the password is right
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            #then we log the user in
            login_user(user, remember=form.remember.data)
            #and take them to the next page
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        #if some data is incorrect, the message is flashed
        if not user or not bcrypt.check_password_hash(user.password, form.password.data):
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


#logs the user out
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app = create_app()
    app.run()
