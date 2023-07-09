from rest_framework import serializers
from sn_app.models import User


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        label="confirm_password", 
        style = {"input_type": "password"},
        trim_whitespace = False,
        write_only = True
        )
    
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "confirm_password"
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            }
        
    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('confirm_password')

        if password1 != password2:
            msg = "Access Denied: Passwords don't match!"
            raise serializers.ValidationError(msg, code="authorization")
    
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'] 
        )

        return user

