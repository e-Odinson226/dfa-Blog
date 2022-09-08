from django.urls import path

from .views import *

urlpatterns = [
    path("users/", UserList.as_view(), name="user-list-api"),
    path("users/<int:pk>", UserDetail.as_view(), name="user-detail-api"),
    path("", PostList.as_view(), name="post-list-api"),
    path("<int:pk>", PostDetail.as_view(), name="post-detail-api"),
]
