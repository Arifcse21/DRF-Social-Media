from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from sn_app.serializers import ProfileSerializer
from sn_app.models import Profile, User
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from sn_app.utils import (SafeJWTAuthentication, decode_uuid_from_jwt)
# from sn_app.decorators import JWTRequired


class UserProfileView(ViewSet): 
	authentication_classes = [SafeJWTAuthentication, ]

	# @JWTRequired
	@swagger_auto_schema(
		operation_summary="Show user profile",
		operation_description="This api show user profile only if there is a valid jw token"
	)
	def list(self, request):
		uuid = decode_uuid_from_jwt(request.headers["Authorization"])

		try:
			user = get_object_or_404(User, uuid=uuid)
			print(f"Here: {user}")
			profile = get_object_or_404(Profile, user=user)
			print(f"HereP: {profile}")
			first_name = str(user.first_name) or None
			last_name = str(user.last_name) or None

			profile_data = ProfileSerializer(profile).data
			print(f"profile_data: type({profile_data})")
			profile_data["first_name"] = first_name
			profile_data["last_name"] = last_name
			
			api_response = {
				"status": "successful",
				"message": "User profile data",
				"data": profile_data
			}
			return Response(api_response, status=status.HTTP_200_OK)

		except Exception as e:
			api_response = {
				"status": "failed",
				"message": str(e)
			}
			return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
