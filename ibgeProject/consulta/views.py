from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def home(request):
    return Response({'message':"plate' no valid"}, status = status.HTTP_400_BAD_REQUEST)