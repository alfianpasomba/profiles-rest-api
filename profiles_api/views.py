from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloAPIView(APIView):
    serializer_class = serializers.HelloSerializers
    def get(self, request, format=None):
        joblist = [
            "data analyst",
            "data scientist",
            "ml engineer",
            "ai engineer",
        ]

        return Response({"message":"tes api view pertama kali", "data":joblist})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Halo {name}"
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def patch(self, request, pk=None):
        return Response({"method":"PATCH"})
    
    def put(self, request, pk=None):
        return Response({"method":"PUT"})
    
    def delete(self, request, pk=None):
        return Response({"method":"DELETE"})
    

class HelloViewSets(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializers

    def list(self, request):
        mylist = [
            "excel",
            "sql",
            "tableau",
            "power bi",
            "looker studio",
            "python"
        ]

        return Response({"messages":"hallo, ini adalah viewsets","data":mylist})

    def retrieve(self, request, pk=None):
        return Response({"method":"GET"})
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            return Response({"message":f"Hallo {name}"})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def update(self, request, pk=None):
        return Response({"method":"PUT"})
    
    def partial_update(self, request, pk=None):
        return Response({"method":"PATCH"})
    
    def destroy(self, request, pk=None):
        return Response({"method":"DELETE"})

class ProfileViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializers
    queryset = models.UserProfile.objects.all()
    permission_classes = (permissions.UpdateOwnProfile,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email",)

class UserLoginViewSets(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ProfileFeedItemViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileFeedItemSerializers
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfileFeed, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
