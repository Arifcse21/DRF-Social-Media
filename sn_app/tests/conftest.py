import pytest
from rest_framework.test import APIClient
from sn_app.models import User
from sn_app.models import Post
from faker import Faker


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        pass


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def demo_user():
    user = User.objects.create(
        first_name="demo",
        last_name="user",
        username = "demo_user_1",
        email="demo@mail.com",
        password="strongpassword12"
    )

    user.save()

    return user

@pytest.fixture
def demo_post(demo_user):
    faker = Faker()

    post = Post(
        user=demo_user,
        content=faker.text(),
        upvote=10,
        downvote=3,

    )

    post.save()

    return post 
