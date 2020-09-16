from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets , generics , status
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json

@api_view(['GET'])
def welcome(request):
    content = {"message": "Welcome to the BookStore!"}
    return JsonResponse(content)
