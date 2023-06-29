from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from sm_app.serializers import UserSerializer
from sm_app.utils import GenerateJWTokensUtil
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
import uuid



class RegisterUserView(ViewSet):

    @swagger_auto_schema(
        request_body=UserSerializer,
        operation_summary="Register new user",
        operation_description="This api registers new user and return access jw token"
    )

    def create(self, request):
        user_uuid  = str(uuid.uuid4())
        user_data = {
            "first_name": request.data["first_name"],
            "last_name": request.data["last_name"],
            "email": request.data["email"],
            "username": request.data["username"],
            "password": request.data["password"],
            "uuid": user_uuid,

        }

        serializer = UserSerializer(data=user_data, context={"request": request})

        access_token = GenerateJWTokensUtil.access_token_generator(user_uuid)
        refresh_token = GenerateJWTokensUtil.refresh_token_generator(user_uuid)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            api_response = {
                "status": "successful",
                "message": "New user registered",
                "access_token": str(access_token),
            }

            return Response(api_response, status=status.HTTP_201_CREATED)
        

