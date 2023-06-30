from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from sm_app.utils import SafeJWTAuthentication


class LoginView(ViewSet):

    def create(self, request):

        login_data = request.data
        
    

