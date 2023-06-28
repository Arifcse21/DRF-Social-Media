from django.db import models
from django.contrib.auth import get_user_model
from sm_app.utils import Base64Field


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    pfp = Base64Field()     # take image as base64 string
    bio = models.TextField(max_length=2000, null=True, blank=True)
    sm_links = models.TextField(max_length=2000, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.get_username()!r}"
    
