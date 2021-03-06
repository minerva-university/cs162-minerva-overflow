from flask import Flask
from application.models import *
from application.api import (
    get_posts_written_by_user,
    get_tag_posts,
    get_post_tags,
)

# from application.api import query_search_posts


def test_prior_db_fill(client: Flask):
    assert [cohort.cohort_name for cohort in db.session().query(Cohort).all()] == [
        "M19",
        "M20",
        "M21",
        "M22",
        "M23",
        "M24",
        "M25",
    ]
    assert [city.city_name for city in db.session().query(City).all()] == [
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
    ]
    assert [tag.tag_name for tag in db.session().query(Tag).all()] == [
        "Food & Drinks",
        "Cafe",
        "Clothes",
        "City Set-Up",
        "Health & Fitness",
        "Sightseeing",
        "Transportation",
        "Visa & Logistic",
        "Financial",
    ]


def test_foreign_keys_integration(client: Flask):

    posts_of_user_db = User.query.filter_by(user_id=1).first().posts
    assert [post.title for post in posts_of_user_db] == [
        "Best Donuts in USA",
        "AWS Loft",
    ]

    posts_of_user_function = get_posts_written_by_user(1)
    assert [post.title for post in posts_of_user_function] == [
        "Best Donuts in USA",
        "AWS Loft",
    ]


def test_many_to_many_relationship(client: Flask):

    db.session.execute(tags_and_posts.insert().values(tag_id=1, post_id=2))
    db.session.execute(tags_and_posts.insert().values(tag_id=3, post_id=2))
    db.session.execute(tags_and_posts.insert().values(tag_id=1, post_id=1))
    db.session.execute(tags_and_posts.insert().values(tag_id=2, post_id=1))
    db.session.execute(tags_and_posts.insert().values(tag_id=4, post_id=1))

    db.session.commit()
    posts_for_specific_tag = get_tag_posts(1)
    assert [post.title for post in posts_for_specific_tag] == [
        "Best Donuts in USA",
        "AWS Loft",
    ]

    tags_of_specific_post = get_post_tags(1)
    assert [tag.tag_name for tag in tags_of_specific_post] == [
        "Food & Drinks",
        "Cafe",
        "City Set-Up",
    ]

def test_query_search(client: Flask):
    query1 = "donuts"
    query2 = "coworking"

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

    db.session.add(post1)
    db.session.add(post2)

    db.session.execute(tags_and_posts.insert().values(tag_id=1, post_id=2))
    db.session.execute(tags_and_posts.insert().values(tag_id=3, post_id=2))
    db.session.execute(tags_and_posts.insert().values(tag_id=1, post_id=1))
    db.session.execute(tags_and_posts.insert().values(tag_id=2, post_id=1))
    db.session.execute(tags_and_posts.insert().values(tag_id=4, post_id=1))

    db.session.commit()

    donuts_posts = Post.query.msearch(query1, fields=["title", "post_text"])
    coworking_posts = Post.query.msearch(query2, fields=["title", "post_text"])

    assert list(set([post.title for post in donuts_posts])) == ["Best Donuts in USA"]
    assert list(set([post.title for post in coworking_posts])) == ["AWS Loft"]