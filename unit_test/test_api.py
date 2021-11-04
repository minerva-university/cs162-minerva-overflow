from flask import json


def test_initialize_server(client):
    """test that server is running"""
    rv = client.get("/")
    assert rv.data == b"Server is running"


def test_create_user(client):
    """test that we can create a new user"""
    rv = client.post(
        "/users",
        json={
            "user": {
                "user_name": "ZheniaMagic",
                "user_password": "Minerva",
                "first_name": "Evgeniia",
                "surname": "Buzulukova",
                "email": "evgeniia@uni.minerva.edu",
                "cohort_id": 5,
                "about_me": "I love coding",
            }
        },
    )
    assert rv.status_code == 201
    assert "User added successfully" in str(rv.data)


def test_create_wrong_user(client):
    """test that if the json is of the wrong format or doesn't exist, it will return a 400 error"""
    rv = client.post(
        "/users",
        json={
            "user_name": "ZheniaMagic",
            "user_password": "Minerva",
            "first_name": "Evgeniia",
            "surname": "Buzulukova",
            "email": "evgeniia@uni.minerva.edu",
            "cohort_id": 5,
            "about_me": "I love coding",
        },
    )
    assert rv.status_code == 400
    rv = client.post("/users", json={})
    assert rv.status_code == 400


def test_create_post(client):
    """test that we can create a new post"""
    rv = client.post(
        "/posts",
        json={
            "post": {"user_id": 1, "city_id": 1, "title": "Hi", "post_text": "hello"}
        },
    )
    assert rv.status_code == 201
    assert "Post added successfully" in str(rv.data)


def test_create_wrong_post(client):
    """test that if the json is of the wrong format or doesn't exist, it will return a 400 error"""
    rv = client.post(
        "/posts",
        json={"user_id": 1, "city_id": 1, "title": "Hi", "post_text": "hello"},
    )
    assert rv.status_code == 400
    rv = client.post("/posts", json={})
    assert rv.status_code == 400


def test_get_tags(client):
    """test that the tags we already have exist"""
    rv = client.get("/tags")
    assert rv.status_code == 201
    assert "Food & Drinks" in str(rv.data)
    assert "City Set-Up" in str(rv.data)


def test_create_tag(client):
    """test that we can create a new tag"""
    rv = client.post(
        "/tags",
        json={"tag": {"tag_name": "Biking"}},
    )
    assert rv.status_code == 201
    assert "Tag added successfully" in str(rv.data)


def test_create_wrong_tag(client):
    """test that if the json is of the wrong format or doesn't exist, it will return a 400 error"""
    rv = client.post(
        "/tags",
        json={"tag_name": "Biking"},
    )
    assert rv.status_code == 400
    rv = client.post("/tags", json={})
    assert rv.status_code == 400


def test_get_cities(client):
    """test that the cities we already have are returned"""
    rv = client.get("/cities")
    assert rv.status_code == 201
    assert "Berlin" in str(rv.data)
    assert "San Francisco" in str(rv.data)


def test_get_cohorts(client):
    rv = client.get("/cohorts")
    assert rv.status_code == 201
    assert (
        "M19" in str(rv.data)
        and "M20" in str(rv.data)
        and "M22" in str(rv.data)
        and "M23" in str(rv.data)
    )
