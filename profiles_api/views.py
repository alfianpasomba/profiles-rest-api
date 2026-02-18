from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

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