import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def welcome(request):
    content = {"message": "Welcome to the DRF!"}
    return JsonResponse(content)

@api_view(['GET'])
def foo(request):
    return JsonResponse({'foo':'bar'})


# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>Minha Pagina</title></html>')
