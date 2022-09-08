# from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register("", PostViewSet, basename="posts")
router.register("users", UserViewSet, basename="users")

urlpatterns = router.urls


# urlpatterns = [
#    path("users/", UserList.as_view(), name="user-list-api"),
#    path("users/<int:pk>", UserDetail.as_view(), name="user-detail-api"),
#    path("", PostList.as_view(), name="post-list-api"),
#    path("<int:pk>", PostDetail.as_view(), name="post-detail-api"),
# ]
