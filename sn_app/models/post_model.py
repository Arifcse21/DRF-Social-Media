from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
    content = models.TextField()
    upvote = models.PositiveIntegerField(null=True, blank=True)
    downvote = models.PositiveIntegerField(null=True, blank=True)
    is_archieved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user}: {self.slug}"
    
