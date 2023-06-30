from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sm_app.views import (
    RegisterUserView,
    LoginView,
)
router = DefaultRouter()

router.register('register', RegisterUserView, basename="register-user")
router.register('login', LoginView, basename='login-user')



urlpatterns = [
    path("api/v1/", include(router.urls)),    
]