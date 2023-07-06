from rest_framework import routers
from sm_app.views import UserFollowingView



class CustomRouter(routers.DefaultRouter):

    def get_routes(self, viewset):
        routes = super().get_routes(viewset)

        custom_routes = [
            routers.Route(
                url=r"^{prefix}/{lookup}/follow{trailing_slash}$",
                mapping={"post": "follow"},
                name="{basename}-follow",
                detail=True,
                initkwargs={}
            ),

            routers.Route(
                url=r"^{prefix}/{lookup}/unfollow{trailing_slash}$",
                mapping={"post": "unfollow"},
                name="{basename}-unfollow",
                detail=True,
                initkwargs={}
            )
        ]

        return routes + custom_routes
    