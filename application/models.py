import datetime
from sqlalchemy import event
from sqlalchemy.sql.schema import Table
from sqlalchemy.engine.base import Connection
from dataclasses import dataclass

from application.extensions import db, guard


""" 
    Table for tags and posts
     :param tag_id: unique tag id
     :param post_id: unique post id
"""
tags_and_posts = db.Table(
    "tags_and_posts",
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.tag_id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.post_id"), primary_key=True),
)


""" 
    Table for users' favorite posts
     :param user_id: unique user id
     :param post_id: unique post id
"""
user_favorites = db.Table(
    "user_favorites",
    db.Column("user_id", db.Integer, db.ForeignKey("users.user_id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.post_id"), primary_key=True),
)


@dataclass
class Tag(db.Model):
    """
    Table for tags
     :param tag_id: unique tag id
     :param tag_name: tag name
     :param posts: posts that are written with the mention of specific tag
    """

    # adding specification to create json object
    tag_id: int
    tag_name: str

    __tablename__ = "tags"

    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name = db.Column(db.String(), nullable=False)
    posts = db.relationship(
        "Post",
        secondary=tags_and_posts,
        lazy=True,
        backref=db.backref("posts_with_tag", lazy=True),
    )

    def __init__(self, tag_name: str):
        self.tag_name = tag_name


@dataclass
class Post(db.Model):
    """
    Table for posts
     :param post_id: unique post id
     :param user_id: id of the user, who wrote the post
     :param city_id: id of the city, for which this post was written
     :param title: title of the post
     :param post_text: content of the post
     :param upvotes: number of upvotes for this post
     :param edited: boolean if the post was edited
     :param created_at: datetime of the post creation
     :param tags: tags mentioned in this post
     :param comments: comments written to this post
     :param: favorite_of: users, who chose this post as their favorite
    """

    # adding specification to create json object
    post_id: int
    user_id: int
    city_id: int
    title: str
    post_text: str
    upvotes: int
    edited: bool
    created_at: datetime.datetime
    tags: Tag

    __tablename__ = "posts"
    __searchable__ = ["title", "post_text"]

    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey("cities.city_id"), nullable=False)
    title = db.Column(db.String(), nullable=False)
    post_text = db.Column(db.String(), nullable=False)
    upvotes = db.Column(db.Integer, nullable=False, default=0)
    edited = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    tags = db.relationship(
        "Tag",
        secondary=tags_and_posts,
        lazy="subquery",
        backref=db.backref("tags_for_post", lazy=True),
    )
    comments = db.relationship("Comment", backref="comments_for_post", lazy="subquery")
    favorite_of = db.relationship(
        "User",
        secondary=user_favorites,
        lazy="subquery",
        backref=db.backref("users_favorited_post", lazy=True),
    )

    def __init__(
        self,
        user_id: int,
        city_id: int,
        title: str,
        post_text: str,
        upvotes: int = 0,
        edited: bool = False,
        created_at: datetime.datetime = None,
    ):
        self.user_id = user_id
        self.city_id = city_id
        self.title = title
        self.post_text = post_text
        self.upvotes = upvotes
        self.edited = edited
        if created_at is not None:
            self.created_at = created_at


@dataclass
class User(db.Model):
    """
    Table for users
     :param user_id: unique user id
     :param username: username of the particular user
     :param password: password of a particular user (no encryption is used as of now)
     :param fisrt_name: first name of the user
     :param surname: surname of the user
     :param email: user's email address
     :param cohort_id: user's cohort id
     :param about_me: user's description of themselves
     :param access_privilege: boolean if the user has admin rights
     :param posts: posts, written by the user
     :param comments: comments, written by the user
     :param user_favorite_posts: user's favorite posts
    """

    # adding specification to create json object
    user_id: int
    username: str
    password: str
    first_name: str
    surname: str
    email: str
    cohort_id: int
    about_me: str
    access_privilege: bool
    is_active: bool
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    surname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    cohort_id = db.Column(
        db.Integer, db.ForeignKey("cohorts.cohort_id"), nullable=False
    )
    about_me = db.Column(db.String(), nullable=False)
    access_privilege = db.Column(db.Boolean, nullable=False, default=0)
    is_active = db.Column(db.Boolean, default=True, server_default="true")
    posts = db.relationship("Post", backref="users", lazy="subquery")
    comments = db.relationship("Comment", backref="users", lazy=True)
    user_favorite_posts = db.relationship(
        "Post",
        secondary=user_favorites,
        lazy=True,
        backref=db.backref("user_favorite_posts", lazy=True),
    )

    def __init__(
        self,
        username: str,
        password: str,
        first_name: str,
        surname: str,
        email: str,
        cohort_id: int,
        about_me: str,
        access_privilege: bool = 0,
        is_active: bool = 1,
    ):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.cohort_id = cohort_id
        self.about_me = about_me
        self.access_privilege = access_privilege
        self.is_active = is_active

    @property
    def rolenames(self):
        try:
            return self.roles.split(",")
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.user_id

    def is_valid(self):
        return self.is_active

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.user_id

    def is_valid(self):
        return self.is_active


@dataclass
class City(db.Model):
    """
    Table for cities
     :param city_id: unique city id
     :param city_name: city name
     :param posts: posts that are written with the mention of specific city
    """

    # adding specification to create json object
    city_id: int
    city_name: str

    __tablename__ = "cities"

    city_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String(), nullable=False)
    posts = db.relationship("Post", backref="posts_with_city", lazy=True)


@dataclass
class Cohort(db.Model):
    """
    Table for cohorts
     :param cohort_id: unique cohort id
     :param cohort_name: cohort name
     :param posts: posts that are written with the mention of specific cohort
    """

    # adding specification to create json object
    cohort_id: int
    cohort_name: str

    __tablename__ = "cohorts"

    cohort_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cohort_name = db.Column(db.String(), nullable=False)
    users = db.relationship("User", backref="posts_with_cohort", lazy=True)

    def __init__(self, cohort_name: str):
        self.cohort_name = cohort_name


@dataclass
class Comment(db.Model):
    """
    Table for posts
     :param comment_id: unique comment id
     :param post_id: id of the post, for which the comment was written
     :param user_id: id of the user, who wrote the comment
     :param comment_text: content of the comment
     :param upvotes: number of upvotes for this comment
     :param edited: boolean if the comment was edited
     :param created_at: datetime of the comment creation
    """

    # adding specification to create json object
    comment_id: int
    post_id: int
    user_id: int
    comment_text: str
    upvotes: int
    edited: bool
    created_at: datetime.datetime

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.post_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    comment_text = db.Column(db.String(), nullable=False)
    upvotes = db.Column(db.Integer, nullable=False, default=0)
    edited = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )

    def __init__(
        self,
        post_id: int,
        user_id: int,
        comment_text: str,
        upvotes: int = 0,
        edited: bool = False,
        created_at: datetime.datetime = None,
    ):
        self.post_id = post_id
        self.user_id = user_id
        self.comment_text = comment_text
        self.upvotes = upvotes
        self.edited = edited
        if created_at is not None:
            self.created_at = created_at


def insert_initial_cohorts(target: Table, connection: Connection, **kw):
    for year in range(19, 26):
        cohort_name = "M" + str(year)
        connection.execute(target.insert(), {"cohort_name": cohort_name})


def insert_initial_cities(target: Table, connection: Connection, **kw):
    for city in [
        "General / All",
        "San Francisco, USA",
        "Seoul, Korea",
        "Hyderabad, India",
        "Berlin, Germany",
        "Buenos Aires, Argentina",
        "London, UK",
        "Taipei, Taiwan",
        "Others",
        "Remote",
    ]:
        connection.execute(target.insert(), {"city_name": city})


def insert_initial_tags(target: Table, connection: Connection, **kw):
    for tag in [
        "Food & Drinks",
        "Cafe",
        "Clothes",
        "City Set-Up",
        "Health & Fitness",
        "Sightseeing",
        "Transportation",
        "Visa & Logistic",
        "Financial",
    ]:
        connection.execute(target.insert(), {"tag_name": tag})


def insert_initial_users(target: Table, connection: Connection, **kw):
    user1 = User(
        username="ZheniaMagic",
        password=guard.hash_password("Minerva"),
        first_name="Evgeniia",
        surname="Buzulukova",
        email="evgeniia@uni.minerva.edu",
        cohort_id=5,
        about_me="I love coding",
    )

    user2 = User(
        username="sherlockieee",
        password=guard.hash_password("123"),
        first_name="Ha",
        surname="Tran",
        email="tnp_ha@uni.minerva.edu",
        cohort_id=5,
        about_me="I love boba",
    )

    user3 = User(
        username="yuehan",
        password=guard.hash_password("7817"),
        first_name="Yueh Han",
        surname="Huang",
        email="yhhuang@uni.minerva.edu",
        cohort_id=4,
        about_me="I love boba and coding",
    )

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()


def insert_initial_posts(target: Table, connection: Connection, **kw):

    post1 = Post(
        user_id=1,
        city_id=2,
        title="Best Donuts in USA",
        post_text="Bob's Donuts are so so great. I love them!",
    )
    post2 = Post(
        user_id=1,
        city_id=2,
        title="AWS Loft",
        post_text="Nice coworking space available for free",
    )
    post3 = Post(
        user_id=3,
        city_id=5,
        title="Berlin Swapfiets ????",
        post_text="Good deal to get a bike a move around in Berlin!",
    )
    post4 = Post(
        user_id=3,
        city_id=7,
        title="London Barber School ??????",
        post_text="Get a cheap and decent haircut in London!",
    )
    post5 = Post(
        user_id=3,
        city_id=8,
        title="Ubike in Taipei",
        post_text="Get a city card and rent bike with rate of $1/hr!",
    )
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.commit()


event.listen(Tag.__table__, "after_create", insert_initial_tags)
event.listen(City.__table__, "after_create", insert_initial_cities)
event.listen(Cohort.__table__, "after_create", insert_initial_cohorts)
event.listen(User.__table__, "after_create", insert_initial_users)
event.listen(Post.__table__, "after_create", insert_initial_posts)
