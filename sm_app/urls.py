from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sm_app.views import (
    RegisterUserView,
    LoginView,
    UpdateProfileView,
    UserProfileView
)
router = DefaultRouter()

router.register('register', RegisterUserView, basename="register-user")
router.register('login', LoginView, basename='login-user')
router.register('profile', UserProfileView, basename='user-profile')
router.register('profile/update', UpdateProfileView, basename='update-profile')



urlpatterns = [
    path("api/v1/", include(router.urls)),    
]