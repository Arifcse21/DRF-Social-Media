from rest_framework.serializers import ModelSerializer
from sm_app.models import User

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]
        