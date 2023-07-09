from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from uuid import uuid4


class User(AbstractUser):
    uuid = models.CharField(max_length=40, editable=False, default=uuid4())

    def __repr__(self) -> str:
        return f"{self.username!r}"     # !r is for raw string
    