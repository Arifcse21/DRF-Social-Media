import pytest
from sn_app.models import User

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
            username="test_user_1",
            email="test@mail.com",
            password="istronggpassowarddo12"
        )

        test_user.save()

        test_count = User.objects.count()

        assert test_count == 1

    def test_retrieve_user(self, demo_user):
        user = User.objects.create(
            first_name="rett",
            last_name="user",
            username="retr_user_111",
            email="rett12@mail.com",
            password="superpass12345"
        )

        user.save()

        retrieve_user = User.objects.filter(username=user.username)

        assert len(retrieve_user) == 1
        assert retrieve_user.first().id == 2

    def test_update_user(self, demo_user):
        User.objects.filter(pk=1).update(
            username="updated_demo_user_1"
        )

        user = User.objects.get(id=1)

        assert user.username == "updated_demo_user_1"

    def test_delete_user(self, demo_user):
        new_user = User.objects.create(
            first_name="new",
            last_name="user",
            username="new_user_100",
            email="new3412@mail.com",
            password="superxpass12345"
        )

        new_user.save()

        assert User.objects.count() == 2

        User.objects.filter(pk=1).delete()

        assert User.objects.count() == 1
