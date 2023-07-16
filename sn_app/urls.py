from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sn_app.utils import CustomRouter
from sn_app.views import (
    RegisterUserView,
    LoginView,
    UpdateProfileView,
    UserProfileView,
    UserFollowingView,
    CreatePostView,
    UpdatePostView,
    SinglePostView,
)
router = DefaultRouter()

router.register('register', RegisterUserView, basename="register-user")
router.register('login', LoginView, basename='login-user')
router.register('profile', UserProfileView, basename='user-profile')
router.register('profile/update', UpdateProfileView, basename='update-profile')
router.register('post/create', CreatePostView, basename='create-post')
router.register('post/<slug:slug>', SinglePostView, basename='single-post')
router.register('post/<slug:slug>/update', UpdatePostView, basename='update-post')


custom_router = CustomRouter()

custom_router.register("connection", UserFollowingView, basename="connection")
# .|^ endpoint will be "api/v1/connection/{user_pk}/(un)follow/"

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/", include(custom_router.urls)),
]