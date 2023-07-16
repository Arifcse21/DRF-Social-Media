import pytest 
import unittest
from faker import Faker
from sn_app.models import Post


pytestmark = pytest.mark.django_db


class TestPostModel:

    def test_empty_post(self):
        post = Post.objects.all()

        count = Post.objects.count()

        assert post.count() == count 
    
    def test_create_post(self, demo_user):
        
        faker = Faker()
        test_post = Post(
            user=demo_user,
            title=faker.text(),
            slug=faker.text(),
            is_archieved=False,
            content=faker.text(),
        )
        test_post.save()

        count = Post.objects.count()

        assert count == 1

        assert test_post.user.username is demo_user.username

    def test_retrieve_post(self, demo_post, demo_user):
        post = Post.objects.create(
            user=demo_user,
            title=Faker().text(),
            slug=Faker().text(),
            is_archieved=True,
            content=Faker().text(),
            upvote=3,
            downvote=5
        )
        post.save()

        query = Post.objects.filter(user=demo_user, upvote=3, downvote=5)

        assert query.count() == 1

        assert query.first().id == 2

    def test_update_post(self, demo_post):
        Post.objects.filter(pk=1).update(
            slug="a-good-title-really-attracts-readers?",
            upvote=10,
            is_archieved=True
        )
        update_post = Post.objects.get(pk=1)

        assert update_post.upvote == 10
        assert update_post.is_archieved is True

    def test_delete_post(self, demo_user, demo_post):
        faker = Faker()
        new_post = Post(
            user=demo_user,
            title=faker.text(),
            slug=faker.text(),
            is_archieved=False,
            content=faker.text(),
        )
        new_post.save()
        count = Post.objects.count()

        assert count == 2

        Post.objects.get(pk=1).delete()
        post = Post.objects.all()

        assert post.count() == 1
        assert post.first().id == 2

