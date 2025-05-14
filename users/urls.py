from collections import UserList

from django.urls import path
from .views import UserCreateView, UserDetailView, ChangePasswordView, UserListView

urlpatterns = [
    path('', UserCreateView.as_view(), name='create_user'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('logout/', UserCreateView.as_view(), name='logout'),
    path('users/', UserListView.as_view(), name='user_list'),
]
