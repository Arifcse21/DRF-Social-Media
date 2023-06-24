from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4


def maintain_serial():
    last_entry = User.objects.all().order_by('id').last()
    if last_entry:
        return last_entry.id + 1
    return 1


class User(AbstractUser):
    id = models.AutoField(default=maintain_serial)
    uuid = models.UUIDField(default=uuid4(), null=True, blank=True)
    connections = models.ManyToManyField(get_user_model(), null=True, blank=True)
    

    def __repr__(self) -> str:
        return f"{self.username!r}"     # !r is for raw string
    