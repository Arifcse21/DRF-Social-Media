from rest_framework.response import Response
from rest_framework import status
from sm_app.serializers import ProfileSerializer
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from sm_app.models import Profile
from django.contrib.auth import get_user_model
from sm_app.utils import (SafeJWTAuthentication, decode_uuid_from_jwt)
from sm_app.decorators import JWTRequired


class UpdateProfileView(ViewSet):
    authentication_classes = [SafeJWTAuthentication, ]

    @JWTRequired
    @swagger_auto_schema(
        request_body=ProfileSerializer,
        operation_summary="Update user profile",
        operation_description="This api update existing user profile"
    )
    def create(self, request):
        uuid = decode_uuid_from_jwt(request.headers["Authorization"])
        profile_data = request.data

        try:
            user_profile = Profile.objects.filter(user__uuid=uuid)
            if user_profile.exists():
                user_profile = user_profile.first()
                serializer = ProfileSerializer(user_profile, data=profile_data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                api_response = {
                    "status": "successful",
                    "message": "User profile updated",
                    "data": serializer.data
                }
                return Response(api_response, status=status.HTTP_200_OK)
                
        except Exception as e:
            api_response = {
                "status": "failed",
                "message": "User not found!",
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
        