from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=maodels.CASCADE, null=True, blank=True)
    content = models.TextField()
    upvote  = models.PositiveBigIntegerField(null=True, blank=True)
    downvote = models.PositiveBigIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.user}: {self.id}"
    
    

