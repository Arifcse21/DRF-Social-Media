from rest_framework.response import Response
from rest_framework import status
from sn_app.serializers import ProfileUpdateSerializer
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from sn_app.models import Profile
from django.contrib.auth import get_user_model
from sn_app.utils import (SafeJWTAuthentication, decode_uuid_from_jwt)
# from sn_app.decorators import JWTRequired
from django.shortcuts import get_object_or_404


class UpdateProfileView(ViewSet):
    authentication_classes = [SafeJWTAuthentication, ]

    # @JWTRequired
    @swagger_auto_schema(
        request_body=ProfileUpdateSerializer,
        operation_summary="Update user profile",
        operation_description="This api update existing user profile"
    )
    def create(self, request):
        uuid = decode_uuid_from_jwt(request.headers["Authorization"])
        profile_data = request.data


        try:
            user = get_object_or_404(get_user_model(), uuid=uuid)
            user_profile = get_object_or_404(Profile, user=user)
            serializer = ProfileUpdateSerializer(user_profile, data=profile_data, partial=True, context={'uuid': uuid})
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
