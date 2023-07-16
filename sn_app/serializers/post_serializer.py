from rest_framework import serializers
from sn_app.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
