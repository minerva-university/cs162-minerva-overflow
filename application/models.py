from app import db
import datetime
from sqlalchemy import event

tags_and_posts = db.Table('tags_and_posts',
                          db.Column('tag_id', db.Integer, db.ForeignKey('tags.tag_id'), primary_key=True),
                          db.Column('post_id', db.Integer, db.ForeignKey('posts.post_id'), primary_key=True))

user_favorites = db.Table('user_favorites',
                          db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'), primary_key=True),
                          db.Column('post_id', db.Integer, db.ForeignKey('posts.post_id'), primary_key=True))


class Tag(db.Model):
    __tablename__ = 'tags'

    tag_id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(), nullable=False)
    posts = db.relationship('Post', secondary=tags_and_posts, lazy='subquery',
                            backref=db.backref('tags', lazy=True))

    def __init__(self, tag_name: str):
        self.tag_name = tag_name


class Post(db.Model):
    __tablename__ = 'posts'

    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'), nullable=False)
    title = db.Column(db.String(), nullable=False)
    post_text = db.Column(db.String(), nullable=False)
    upvotes = db.Column(db.Integer, nullable=False)
    edited = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    tags = db.relationship('Tag', secondary=tags_and_posts, lazy='subquery',
                           backref=db.backref('posts', lazy=True))
    comments = db.relationship('Comment', backref='posts', lazy='subquery')
    favorite_of = db.relationship('User', secondary=user_favorites, lazy='subquery',
                                  backref=db.backref('posts', lazy=True))

    def __init__(self, user_id: int, city_id: int, title: str, post_text: str,
                 upvotes: int = 0, edited: bool = False,
                 created_at: datetime.datetime = datetime.datetime.now()):
        self.user_id = user_id
        self.city_id = city_id
        self.title = title
        self.post_text = post_text
        self.upvotes = upvotes
        self.edited = edited
        self.created_at = created_at


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    user_password = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    surname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    cohort_id = db.Column(db.Integer, db.ForeignKey('cohorts.cohort_id'), nullable=False)
    about_me = db.Column(db.String(), nullable=False)
    access_privilege = db.Column(db.Boolean, nullable=False)
    posts = db.relationship('Post', backref='users', lazy=True)
    comments = db.relationship('Comment', backref='users', lazy=True)
    favorite_of = db.relationship('Post', secondary=user_favorites, lazy='subquery',
                                  backref=db.backref('users', lazy=True))

    def __init__(self, user_name: str, user_password: str,
                 first_name: str, surname: str, email: str, cohort_id: int,
                 about_me: str, access_privilege: bool = 0):
        self.user_name = user_name
        self.user_password = user_password
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.cohort_id = cohort_id
        self.about_me = about_me
        self.access_privilege = access_privilege


class City(db.Model):
    __tablename__ = 'cities'

    city_id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(), nullable=False)
    posts = db.relationship('Post', backref='cities', lazy=True)


class Cohort(db.Model):
    __tablename__ = 'cohorts'

    cohort_id = db.Column(db.Integer, primary_key=True)
    cohort_name = db.Column(db.String(), nullable=False)
    users = db.relationship('User', backref='cohorts', lazy=True)

    def __init__(self, cohort_name: str):
        self.cohort_name = cohort_name


class Comments(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    comment_text = db.Column(db.String(), nullable=False)
    upvotes = db.Column(db.Integer, nullable=False)
    edited = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, post_id: int, user_id: int, comment_text: str,
                 upvotes: int = 0, edited: bool = False,
                 created_at: datetime.datetime = datetime.datetime.now()):
        self.post_id = post_id
        self.user_id = user_id
        self.comment_text = comment_text
        self.upvotes = upvotes
        self.edited = edited
        self.created_at = created_at


def insert_initial_cohorts():
    for year in range(19, 26):
        cohort_name = 'M' + str(year)
        db.session.add(Cohort(cohort_name=cohort_name))


def insert_initial_cities():
    for city in ['General / All', 'San Francisco, USA', 'Seoul, Korea',
                 'Hyderabad, India', 'Berlin, Germany', 'Buenos Aires, Argentina',
                 'London, UK', 'Taipei, Taiwan', 'Others', 'Remote']:
        db.session.add(City(city_name=city))


def insert_initial_tags():
    for tag in ['Food & Drinks', 'Cafe', 'Clothes',
                'City Set-Up', 'Health & Fitness', 'Sightseeing',
                'Transportation', 'Visa & Logistic', 'Financial']:
        db.session.add(Tag(tag_name=tag))
    db.session.commit()


event.listen(Cohort, 'after_create', insert_initial_cohorts)
event.listen(City, 'after_create', insert_initial_cities)
event.listen(Tag, 'after_create', insert_initial_tags)
