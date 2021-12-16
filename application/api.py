from flask import Blueprint, request, abort, Response, jsonify
import flask

# import flask_whooshalchemy as wa
from typing import List, Tuple
from application.models import *
from application.extensions import guard
import flask_praetorian

api = Blueprint("api", __name__)


@api.route("/")
def hello_world():
    return "Hello world"


@api.route("/api/")
def index():
    return "Server is running"


@api.route("/api/users", methods=["GET"])
def get_users() -> Tuple[Response, int]:
    """Function to get all users from the database"""
    users = User.query.all()
    return (jsonify(users), 201)


@api.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id: int) -> Tuple[Response, int]:
    """Function to get post from its id in the database"""
    user = User.query.filter_by(user_id=int(user_id)).first()
    if not user:
        abort(400, "User doesn't exist")
    return (jsonify(user), 201)


@api.route("/api/users", methods=["POST"])
def add_user() -> Tuple[Response, int]:
    """Function to add a new user to the database"""
    if not request.json or not "user" in request.json:
        abort(400, "Request form incorrect")
    existing_user = User.query.filter_by(
        username=request.json["user"]["username"]
    ).first()
    if existing_user:
        abort(403, "Username already exists")
    existing_email = User.query.filter_by(email=request.json["user"]["email"]).first()
    if existing_email:
        abort(403, "Email already exists")
    username=request.json["user"]["username"]
    password=guard.hash_password(request.json["user"]["password"])
    email=request.json["user"]["email"]
    first_name=request.json["user"]["first_name"]
    surname=request.json["user"]["surname"]
    cohort_id=request.json["user"]["cohort_id"]
    about_me=request.json["user"]["about_me"]
    user = User(username=username,password=password,email=email, first_name=first_name, surname=surname,cohort_id=cohort_id,about_me=about_me)
    db.session.add(user)
    db.session.commit()
    return (
        jsonify(
            {"message": "User added successfully", "status": "SUCCESS", "user": user}
        ),
        201,
    )

@api.route("/api/posts", methods=["GET"])
def get_all_posts() -> Tuple[Response, int]:
    """Function to get all posts from the database"""
    posts = Post.query.all()
    return (jsonify(posts), 201)


@api.route("/api/posts", methods=["POST"])
def add_post() -> Tuple[Response, int]:
    """Function to add a new post to the database"""
    if not request.json or not "post" in request.json:
        abort(400, "Request form incorrect")
    post = Post(**request.json["post"])
    db.session.add(post)
    db.session.commit()
    return (
        jsonify(
            {"message": "Post added successfully", "status": "SUCCESS", "post": post}
        ),
        201,
    )


@api.route("/api/posts/<int:post_id>", methods=["GET"])
def get_post(post_id: int) -> Tuple[Response, int]:
    """Function to get post from its id in the database"""
    post = Post.query.filter_by(post_id=int(post_id)).first()
    if not post:
        abort(400, "Post doesn't exist")
    return (jsonify(post), 201)


@api.route("/api/posts/<int:post_id>", methods=["PUT"])
@flask_praetorian.auth_required
def edit_post(post_id: int) -> Tuple[Response, int]:
    """Function to edit post in the database"""
    post = Post.query.filter_by(post_id=int(post_id)).first()
    if not post:
        abort(400, "Post doesn't exist")
    new_post_dict = request.json["post"]
    for item, value in post.__dict__.items():
        new_entry = new_post_dict.get(item)
        if new_entry and new_entry != value:
            setattr(post, item, new_entry)
    post.edited = True
    db.session.commit()
    return (
        jsonify({"message": f"Post {post.post_id} updated successfully", "post": post}),
        201,
    )


@api.route("/api/posts/<int:post_id>", methods=["DELETE"])
@flask_praetorian.auth_required
def delete_post(post_id: int) -> Tuple[Response, int]:
    """Function to delete post in the database"""
    post = Post.query.filter_by(post_id=int(post_id)).first()
    if not post:
        abort(400, "Post doesn't exist")
    db.session.delete(post)
    db.session.commit()
    return (
        jsonify({"message": f"Post {post_id} deleted successfully"}),
        201,
    )


@api.route("/api/tags", methods=["GET"])
@flask_praetorian.auth_required
def get_tags() -> Tuple[Response, int]:
    """Function to get all tags from the database"""
    tags = Tag.query.all()
    return (jsonify(tags), 201)


@api.route("/api/tags", methods=["POST"])
@flask_praetorian.auth_required
def add_tag() -> Tuple[Response, int]:
    """Function to add a new tag to the database"""
    if not request.json or not "tag" in request.json:
        abort(400, "Request form incorrect")
    tag = Tag(**request.json["tag"])
    db.session.add(tag)
    db.session.commit()
    return (
        jsonify({"message": "Tag added successfully", "status": "SUCCESS", "tag": tag}),
        201,
    )


@api.route("/api/posts/<int:post_id>/tags/<int:tag_id>", methods=["POST"])
@flask_praetorian.auth_required
def add_tag_to_post(tag_id: int, post_id: int) -> Tuple[Response, int]:
    """Function to add tag to the post in the database"""
    db.session.execute(tags_and_posts.insert().values(tag_id=tag_id, post_id=post_id))
    db.session.commit()
    return (
        jsonify(
            {
                "message": f"Tag {tag_id} added to post {post_id} successfully",
                "status": "SUCCESS",
            }
        ),
        201,
    )


'''
@api.route("/api/posts/<post_id>", methods=["POST"])
def upvote_post(post_id: int) -> Response:
    """Function to upvote post"""
    post = Post.query.filter_by(post_id=int(post_id)).first()
    post.upvotes += 1
    db.session.commit()

    return redirect(url_for("index"))
'''


@api.route("/api/cohorts", methods=["GET"])
def get_cohorts() -> Tuple[Response, int]:
    """Get all cohorts in database"""
    cohorts = Cohort.query.all()
    return (jsonify(cohorts), 201)


@api.route("/api/cities", methods=["GET"])
def get_cities() -> Tuple[Response, int]:
    """Get all cities in database"""
    cities = City.query.all()
    return (jsonify(cities), 201)


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


def get_posts_by_cohort(cohort_id: int) -> List[Post]:
    return Cohort.query.filter_by(cohort_id=cohort_id).first().posts


# def query_search_posts(query: str) -> List[Post]:
#     return Post.query.whoosh_search(query).all()


@api.route("/api/login", methods=["POST"])
def login():
    """
    Logs a user in by parsing a POST request containing user credentials and
    issuing a JWT token.
    .. example::
       $ curl http://localhost:5000/api/login -X POST \
         -d "{"username":"Yasoob","password":"strongpassword"}"
    """
    req = flask.request.get_json(force=True)
    username = req.get("username", None)
    password = req.get("password", None)
    user = guard.authenticate(username, password)
    ret = {"access_token": guard.encode_jwt_token(user)}
    return ret, 200

@api.route("/api/refresh", methods=["POST"])
def refresh():
    """
    Refreshes an existing JWT by creating a new one that is a copy of the old
    except that it has a refrehsed access expiration.
    .. example::
       $ curl http://localhost:5000/api/refresh -X GET \
         -H "Authorization: Bearer <your_token>"
    """
    print("refresh request")
    old_token = request.get_data()
    new_token = guard.refresh_jwt_token(old_token)
    ret = {"access_token": new_token}
    return ret, 200


@api.route("/api/protected")
@flask_praetorian.auth_required
def protected():
    """
    A protected endpoint. The auth_required decorator will require a header
    containing a valid JWT
    .. example::
       $ curl http://localhost:5000/api/protected -X GET \
         -H "Authorization: Bearer <your_token>"
    """
    return {
        "message": f"protected endpoint (allowed user {flask_praetorian.current_user().username})"
    }
