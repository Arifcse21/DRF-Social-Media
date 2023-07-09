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
            content=faker.text(),
        )
        test_post.save()

        count = Post.objects.count()

        assert count == 1

        assert test_post.user.username is demo_user.username

    def test_retrieve_post(self, demo_post, demo_user):
        post = Post.objects.create(
            user=demo_user,
            content=Faker().text(),
            upvote=3,
            downvote=5
        )
        post.save()

        query = Post.objects.filter(user=demo_user, upvote=3, downvote=5)

        assert query.count() == 1

        assert query.first().id == 2

    def test_update_post(self, demo_post):
        pass





