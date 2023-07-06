from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from sm_app.serializers import FollowingSerializer
from sm_app.models import Profile, User
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from sm_app.utils import (SafeJWTAuthentication, decode_uuid_from_jwt)
from sm_app.decorators import JWTRequired
from rest_framework.decorators import action


class UserFollowingView(ViewSet): 
    authentication_classes = [SafeJWTAuthentication, ]
    queryset = User.object.all()
    
    @action(detail=True, method="post") 
    @JWTRequired
    @swagger_auto_schema(
        operation_summary="Follow a user",
        operation_description="This api let a user follow another user",
        responses={
            "200": "You are now following this user",
            "400": "You cant follow yourself or already following this user"
        }
    )
    def follow(self, request, pk=None):
        uuid = decode_uuid_from_jwt(request.headers["Authorization"])
        
        try:
            user = self.get_object()
            follower = request.user

            if user == follower:
                api_response = {}
                api_response["status"] = "error"
                api_response["message"] = "you cant follow yourself!"
                return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
            
            
            profile = get_object_or_404(Profile, user=follower)
            followings_ids = profile.following.values_list("id", flat=True)
            # to_follow = get_object_or_404(User, pk=pk)

            if pk in followings_ids:
                api_response = {}
                api_response["status"] = "error"
                api_response["message"] = "you are already following this user"

                return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
            
            profile.following.add(pk)       # it takes both ids(*ids) and objects(*users)
            
            api_response = {}
            api_response["status"] = "successful"
            api_response["message"] = "you start following this user now"
            api_response["following"] = FollowingSerializer(profile).data

            return Response(api_response, status=status.HTTP_200_OK)


        except Exception as e:
            api_response = {}
            api_response["status"] = "failed"
            api_response["message"] = str(e)
            
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
        

