from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TestView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, *args, **kwargs):
        # print(request.auth)
        return Response(dir(request.user),status=status.HTTP_200_OK)