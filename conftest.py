import pytest
from flask import Flask
from application.app import create_app
from application.extensions import db
from application.models import *


@pytest.fixture
def client() -> Flask:
    app = create_app()

    app.config["TESTING"] = True
    app.testing = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"

    client = app.test_client()
    with app.app_context():
        db.create_all()

        user1 = User(
            user_name="ZheniaMagic",
            user_password="Minerva",
            first_name="Evgeniia",
            surname="Buzulukova",
            email="evgeniia@uni.minerva.edu",
            cohort_id=5,
            about_me="I love coding",
        )

        user2 = User(
            user_name="sherlockieee",
            user_password="123",
            first_name="Ha",
            surname="Tran",
            email="tnp_ha@uni.minerva.edu",
            cohort_id=5,
            about_me="I love boba",
        )
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
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(post1)
        db.session.add(post2)

        db.session.commit()
    yield client
    with app.app_context():
        db.drop_all()
