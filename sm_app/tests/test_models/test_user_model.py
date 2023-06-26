import pytest
from sm_app.models import User

pytestmark = pytest.mark.django_db


class TestUserModel:

    def test_empty_user(self):
        users = User.objects.all().count()

        assert users == 0

        count = User.objects.count()

        assert users == count

    def test_create_user(self):
        test_user = User.objects.create(
        first_name="test",
        last_name="user",
        email="test@mail.com",
        )

        test_user.save()

        test_count = User.objects.count()

        assert test_count == 1
        