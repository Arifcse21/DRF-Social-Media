from rest_framework.response import Response
from rest_framework import status
from sm_app.serializers import ProfileSerializer
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model


class UpdateProfileView(ViewSet):

    @swagger_auto_schema(
        request_body=ProfileSerializer,
        operation_summary="Register new user",
        operation_description="This api registers new user and return access jw token"
    )
    def update(self, request, uuid):
        
        profile_data = request.data

        try:
            user = get_user_model().objects.filter(uuid=uuid)
            if user.exists():
                user = user.first()

                serializer = ProfileSerializer(user, data=profile_data)
                if serializer.is_valid(raise_exception=True):
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
        