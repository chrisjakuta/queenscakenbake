from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from .models import CustomUser
from django.http import Http404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from user.permissions import UserPermissions
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from user.serializers import (
    UserFrontendSerializer,
    UserRetrieveSerializer,
    UserSerializer,
    ConsumerFrontEndSerializer,
)

# TODO : add Post method on UserModelView class
# TODO : 

class UserModelView(APIView):
    """
    The top level view for querying CustomUser instances.
    """
    lookup_field = 'username'
    permission_classes = [
        UserPermissions,
        IsAuthenticatedOrReadOnly,
    ]

    def get_object(self, username):
        user = CustomUser.objects.get(username=username)
        try:
            return user if not user.is_superuser else None
        except CustomUser.DoesNotExist:
            return None

    def get(self, request, username, format=None):

        user = self.get_object(username)
        if user == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.user.is_authenticated and request.user.username == username:
            serializer = UserFrontendSerializer(user)
            return Response(serializer.data)
        serializer = UserRetrieveSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, username, format=None):

        user = self.get_object(username)
        if user == None:
            return Response(status.HTTP_403_FORBIDDEN)
        serializer = UserFrontendSerializer(user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = UserFrontEndSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserQuerySetView(viewsets.ModelViewSet):
    
#     serializer_class = UserFrontendSerializer
#     queryset = [user for user in CustomUser.objects.all() if not user.is_superuser]
#     permission_classes = [IsAuthenticated]

class CustomUserModelViewSet(viewsets.ModelViewSet):

    model = CustomUser
    permission_classes = [
        UserPermissions,
        IsAuthenticatedOrReadOnly,
    ]
    lookup_field = 'username'
    serializer_class = UserFrontendSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.request.user
        return None
    

