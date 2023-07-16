from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sn_app.serializers import PostSerializer
from sn_app.models import Post, User
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from sn_app.utils import (SafeJWTAuthentication, decode_uuid_from_jwt)
# from sn_app.decorators import JWTRequired


class CreatePostView(ViewSet):
    authentication_classes = [SafeJWTAuthentication, ]

    # @JWTRequired
    @swagger_auto_schema(
        request_body=PostSerializer,
        operation_summary="Create a new post",
        operation_description="This api let a valid user create new post",
        responses={
            "201": "Created a new post",
            "400": "Cannot create new post"
        }
    )
    def create(self, request):
        uuid = decode_uuid_from_jwt(request.headers["Authorization"])

        post_data = request.data

        try:
            payload = {
                "user": get_object_or_404(User, uuid=uuid),
                "title": post_data["title"],
                "content": post_data["content"],
            }

            serializer = PostSerializer(data=payload)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            api_response = {
                "status": "successful",
                "message": f"{request.user} created a new post",
                "data": serializer.data
            }
            return Response(api_response, status=status.HTTP_201_CREATED)
        except Exception as e:
            api_response = {
                "status": "successful",
                "message": str(e)
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
