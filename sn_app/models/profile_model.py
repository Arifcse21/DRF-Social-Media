from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(max_length=2000, null=True, blank=True)
    sm_links = models.TextField(max_length=2000, null=True, blank=True)
    following = models.ManyToManyField('sn_app.User', related_name='connected_users')
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.get_username()!r}"
    
