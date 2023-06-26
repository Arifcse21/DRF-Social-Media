import pytest
from rest_framework.test import APIClient
from sm_app.models import User


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
        email="demo@mail.com",
    )

    user.save()

    return user
