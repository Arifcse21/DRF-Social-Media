from rest_framework import serializers
from sm_app.models import Profile
from django.contrib.auth import get_user_model


class FollowingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = [
            "following",
        ]
        
