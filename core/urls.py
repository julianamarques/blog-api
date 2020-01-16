from django.urls import path
from .views import UsersList, UserDetail, PostsList, PostDetail, PrivatePostsList, PublicPostsList


urlpatterns = [
    path('users/', UsersList.as_view(), name=UsersList.name),
    path('users/<int:id>/', UserDetail.as_view(), name=UserDetail.name),
    path('posts/', PostsList.as_view(), name=PostsList.name),
    path('posts/<int:id>/', PostDetail.as_view(), name=PostDetail.name),
    path('public-posts/', PublicPostsList.as_view(), name=PublicPostsList.name),
    path('private-posts/', PrivatePostsList.as_view(), name=PrivatePostsList.name),
    path('users/post', PublicPostsList.as_view(), name=PublicPostsList.name),
]