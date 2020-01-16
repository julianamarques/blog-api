from django.urls import path
from .views import UserList, UserDetail


urlpatterns = [
    path('users/', UserList.as_view(), name=UserList.name),
    path('users/<int:id>/', UserDetail.as_view(), name=UserDetail.name),
]