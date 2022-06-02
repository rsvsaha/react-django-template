import imp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
# Create your views here.

class HelloWorld(APIView):
    def get(self,request):
        return Response("OK")