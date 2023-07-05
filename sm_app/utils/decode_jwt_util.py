import jwt 
from django.conf import settings

def decode_uuid_from_jwt(token: str) -> str:
    uuid = token.split("Token ")[1]
    decoded_data = jwt.decode(
        uuid, 
        settings.SECRET_KEY,
        algorithms=['HS256']
    )

    return decoded_data["user_uuid"]
