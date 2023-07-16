from rest_framework.response import Response
from rest_framework import status
from sn_app.serializers import PostSerializer
from sn_app.models import Post, User
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from sn_app.utils import (SafeJWTAuthentication, decode_uuid_from_jwt)
from sn_app.views import UpdatePostView
# from sn_app.decorators import JWTRequired


class SinglePostView(UpdatePostView):
    # authentication_classes = [SafeJWTAuthentication, ]

    # @JWTRequired
    @swagger_auto_schema(
        request_body=PostSerializer,
        operation_summary="Read a single post",
        operation_description="This api let *any* user read a post",
        responses={
            "201": "Post data retrieve",
            "400": "Cannot retrieve the post"
        }
    )
    def retrieve(self, request, slug=None):
        # uuid = decode_uuid_from_jwt(request.headers["Authorization"])

        try:
            post = Post.objects.get(slug=slug)
            serializer = PostSerializer(post, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            api_response = {
                "status": "successful",
                "message": f"Post with {serializer.data['title']} data",
                "data": serializer.data
            }
            return Response(api_response, status=status.HTTP_200_OK)
        except Exception as e:
            api_response = {
                "status": "successful",
                "message": str(e)
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
