from rest_framework import serializers
from sn_app.models import Profile
from django.contrib.auth import get_user_model
from sn_app.utils import decode_uuid_from_jwt


class ProfileUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50, trim_whitespace=False)
    last_name = serializers.CharField(max_length=50, trim_whitespace=False)

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "bio",
            "sm_links",
        ]

    def validate(self, attrs):
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')
        bio = attrs.get('bio')
        sm_links = attrs.get('sm_links')

        if not (first_name and last_name and bio and sm_links):
            msg = "Required Fields: All fields data are required!"
            raise serializers.ValidationError(msg, code="authorization")
        else:
            try:
                uuid = self.context['uuid']
                user = get_user_model().objects.get(uuid=uuid)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
            except Exception as e:
                raise serializers.ValidationError(str(e), code="authorization")

        return attrs
