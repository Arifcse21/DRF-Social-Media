from rest_framework.response import Response
from rest_framework import status
from sm_app.serializers import ProfileSerializer
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema


class UpdateProfileView(ViewSet):

    @swagger_auto_schema(
        request_body=ProfileSerializer,
        operation_summary="Register new user",
        operation_description="This api registers new user and return access jw token"
    )
    def update(self, request, uuid):
        pass 