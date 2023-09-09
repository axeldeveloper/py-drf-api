from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets , generics , status
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer

from  api.serializers import  ContatoSerializer
import json

from rest_framework.decorators import api_view
from django.http import JsonResponse

from contato.models import Contato


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContatoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contatos to be viewed or edited.
    """
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContatoList(generics.ListCreateAPIView):

    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class ContatoById(generics.ListCreateAPIView):
    # queryset = Contato.objects.get(pk=self.kwargs['id'])
    serializer_class = ContatoSerializer
    
    def get_queryset(self):
      queryset = Contato.objects.filter(pk=self.kwargs['id'])
      return queryset