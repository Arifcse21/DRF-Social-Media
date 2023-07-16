from sn_app.views import CreatePostView
from rest_framework.response import Response
from rest_framework import status
from sn_app.serializers import PostSerializer
from sn_app.models import Post, User
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from sn_app.utils import (SafeJWTAuthentication, decode_uuid_from_jwt)
# from sn_app.decorators import JWTRequired


class UpdatePostView(CreatePostView):
    # @JWTRequired
    @swagger_auto_schema(
        request_body=PostSerializer,
        operation_summary="Update an existing post",
        operation_description="This api let a valid user update his/her existing post",
        responses={
            "201": "Updated the post",
            "400": "Cannot update the post"
        }
    )
    def update(self, request, slug=None):
        pass