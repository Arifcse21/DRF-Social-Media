from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from sn_app.serializers import LoginSerializer, UserSerializer
from sn_app.utils import GenerateJWTokensUtil
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema



class LoginView(ViewSet):
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=LoginSerializer,
        operation_summary="Login a user",
        operation_description="This api let a user log in with valid username and password"
    )
    def create(self, request):

        login_data = request.data
        serializer = self.serializer_class(data=login_data, context={"request": request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        access_token = GenerateJWTokensUtil.access_token_generator(user.uuid)
        refresh_token = GenerateJWTokensUtil.refresh_token_generator(user.uuid)
        
        api_response = {
            "status": "successful",
            "message": "User logged in successfully",
            "user": UserSerializer(user).data,
            "access_token": access_token, 
            "refresh_token": refresh_token
        }

        return Response(api_response, status=status.HTTP_202_ACCEPTED)
    


    

