from rest_framework import serializers
from sn_app.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"
