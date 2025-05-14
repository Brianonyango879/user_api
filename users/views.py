from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
# Create your views here.
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        new_password = request.data.get('password')
        if new_password:
            user.set_password(new_password)
            user.save()
            return Response({'status': 'password set'})
        return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer