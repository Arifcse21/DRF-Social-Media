import os
import jwt
import datetime
import json
from django.conf import settings


class GenerateJWTokensUtil:
    @staticmethod
    def access_token_generator(data):

        access_token_payload = {
            "user_uuid": data['user_uuid'],
            # "user_type": data['user_type'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=5, minutes=10),
            "iat": datetime.datetime.utcnow()
        }

        access_token = jwt.encode(
            access_token_payload,
            settings.SECRET_KEY,
            algorithm="HS256"
        )

        return access_token

    @staticmethod
    def refresh_token_generator(data):

        payload = {
            "user_uuid": data["user_uuid"],
            # "user_type": data["user_type"],
            "iat": datetime.datetime.utcnow(),
            "nbf": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=3, minutes=5)
        }

        refresh_token = jwt.encode(
            payload,
            settings.REFRESH_TOKEN_SECRET,
            algorithm="HS256"

        )
        return refresh_token