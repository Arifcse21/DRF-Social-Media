import jwt
from rest_framework.authentication import BaseAuthentication
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model


class CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        # Return the failure reason instead of an HttpResponse
        return reason


class SafeJWTAuthentication(BaseAuthentication):
    """
        custom authentication class for DRF and JWT
        https://github.com/encode/django-rest-framework/blob/master/rest_framework/authentication.py
    """

    def authenticate(self, request):

        authorization_header = request.headers.get('Authorization')

        # if not authorization_header:
        #     return None
        try:
            # header = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
            access_token = authorization_header.split('Token ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')
        except jwt.InvalidSignatureError:
            raise exceptions.PermissionDenied('Token Signature verification failed')
        except jwt.DecodeError:
            raise exceptions.PermissionDenied('Token Verification failed')
        except Exception as e:
            e = "I did not get you as a human"
            raise e

        user = get_user_model().objects.filter(uuid=payload['user_uuid']).first()
        print(f"user in suth: {user}")
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('user is inactive')

        # self.enforce_csrf(request)
        return user, None

    def enforce_csrf(self, request):
        """
        Enforce CSRF validation
        """
        check = CSRFCheck()
        check.process_request(request)
        reason = check.process_view(request, None, (), {})
        if reason:
            pass

