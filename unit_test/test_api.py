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
                "user_name": "yaremko.nazar@uni.minerva.edu",
                "user_password": "123",
                "first_name": "Nazar",
                "surname": "Yaremko",
                "email": "yaremko.nazar@uni.minerva.edu",
                "cohort_id": 4,
                "about_me": "I love beer 🍺",
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


def test_unique_users(client):
    """test that if the user already exists, it will return a 403 error"""
    rv = client.post(
        "/users",
        json={
            "user": {
                "user_name": "evgeniia@uni.minerva.edu",
                "user_password": "Minerva",
                "first_name": "Evgeniia",
                "surname": "Buzulukova",
                "email": "evgeniia@uni.minerva.edu",
                "cohort_id": 5,
                "about_me": "I love coding",
            }
        },
    )
    assert rv.status_code == 403


def test_get_specific_user(client):
    """test that we can get a user by their id"""
    rv = client.get("/users/2")
    assert rv.status_code == 201
    assert "Ha" in str(rv.data)
    assert "Tran" in str(rv.data)


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


def test_get_all_posts(client):
    """test that we can get all posts"""
    rv = client.get("/posts")
    assert rv.status_code == 201
    assert "Best Donuts in USA" in str(rv.data)
    assert "AWS Loft" in str(rv.data)


def test_get_specific_post(client):
    """test that we edit a post"""
    rv = client.get("/posts/2")
    assert rv.status_code == 201
    assert "AWS Loft" in str(rv.data)


def test_edit_specific_post(client):
    """test that we edit a post"""
    rv = client.put(
        "/posts/1",
        json={
            "post": {
                "user_id": 2,
                "city_id": 5,
                "title": "Great Restaurant in Kreuzberg!",
                "post_text": "I love Maroush",
            }
        },
    )
    assert rv.status_code == 201
    assert "Post 1 updated successfully" in str(rv.data)
    assert "I love Maroush" in str(rv.data)


def test_delete_specific_post(client):
    """test that we edit a post"""
    rv = client.delete(
        "/posts/1",
    )
    assert rv.status_code == 201
    assert "Post 1 deleted successfully" in str(rv.data)


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
