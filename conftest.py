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

    yield client
    with app.app_context():
        db.drop_all()
